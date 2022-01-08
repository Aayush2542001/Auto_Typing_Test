import pyautogui
import keyboard as kb
import time
import PIL
import pytesseract

# string to print
modifiedString = [None] * 300

# switching to chrome and waiting one second
kb.press_and_release('alt+tab')
time.sleep(1)

# focusing on the current tab of the chrome
pyautogui.moveTo(800, 500) #Test (800, 650) #10fastestfingers (800, 500)
pyautogui.click()


def screenshotToString():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\AAYUSH\PycharmProjects\PycharmTest\fastestfinger.png')

    image = PIL.Image.open('fastestfinger.png')

    image = image.crop((330, 330, 1500, 450))  # Test ((480, 355, 1200, 590)) # 10ff ((330, 330, 1500, 450))
    # image.show()

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # path of Text
    convertedText = pytesseract.image_to_string(image)

    return convertedText


def convertToFinalString(string):
    convertedString = [None] * 300
    x = 0
    i = 0

    while x < len(string):
        if string[x] == '\n':
            if convertedString[i - 1] == ' ':
                x += 1
            else:
                convertedString[i] = ' '
                x += 1
                i += 1
        else:
            convertedString[i] = string[x]
            x += 1
            i += 1

    return convertedString


def pressString(string):
    element = 0
    while string[element] is not None:

        time.sleep(0.03)
        if 65 <= ord(string[element]) <= 90:  # used shift to write upper alphabets
            kb.press_and_release('shift+' + string[element].lower())
            element += 1
        elif string[element] == '?' or string[element] == '!':  # used shift to write upper symbols
            kb.press_and_release('shift+' + string[element])
            element += 1
        else:
            kb.press_and_release(string[element])
            element += 1


for times in range(0, 11):
    imageToText = screenshotToString()
    print(imageToText)

    modifiedString = convertToFinalString(imageToText)
    print(modifiedString)

    pressString(modifiedString)

    time.sleep(0.1)
