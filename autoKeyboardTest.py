import pyautogui
import keyboard as kb
import time
import PIL
import pytesseract

# string to print
modifiedString = [None] * 300
last = time.time()

# switching to chrome and waiting one second
kb.press_and_release('alt+tab')
time.sleep(0.5)

# focusing on the current tab o f the chrome
pyautogui.moveTo(1400, 600)
pyautogui.click()
kb.press_and_release(' ')
time.sleep(0.5)

def screenshotToString():  # takes 2.6 second

    myScreenshot = pyautogui.screenshot()  # 0.4 ms
    myScreenshot.save(r'C:\Users\AAYUSH\PycharmProjects\PycharmTest\screenshot.png')

    image = PIL.Image.open('screenshot.png')  # 0.1 ms

    image = image.crop((645, 453, 1317, 607))

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # path of Text
    convertedText = pytesseract.image_to_string(image)  # 0.3 ms

    return convertedText


def convertToFinalString(string):  # unbelievably takes no second. Not even milisecond
    letters = [']', ')', '<', '«', '"', 'ﬂ', 'é', 'ﬁ']
    convertedString = [None] * 300
    x = 0
    i = 0

    while x < len(string):
        if string[x] in letters:  # letters
            if convertedString[i - 1] != '\n':
                if convertedString[i - 1] == ' ':
                    convertedString[i - 1] = '\n'
                    x += 1
                else:
                    convertedString[i] = '\n'
                    x += 1
                    i += 1
            else:
                x += 1
                continue
        elif string[x] == '1' and convertedString[i - 1] == '\n':  # <1
            x += 1
            continue
        elif string[x] == '\n':  # new line
            if convertedString[i - 1] == ' ' or convertedString[i - 1] == '\n' or convertedString[i - 1] == '-':
                x += 1
                continue
            else:
                convertedString[i] = ' '
                i += 1
                x += 1
        elif string[x] == '!':  # !
            if convertedString[i - 1] == '\n':
                x += 1
                continue
            elif convertedString[i - 1] == '.':
                convertedString[i] = '\n'
                i += 1
                x += 1
            else:
                convertedString[i] = '!'
                i += 1
                x += 1
        elif string[x] == ".":  # .
            if convertedString[i - 1] == ' ':
                convertedString[i - 1] = '.'
                x += 1
            else:
                convertedString[i] = '.'
                i += 1
                x += 1
        else:
            convertedString[i] = string[x]
            i += 1
            x += 1

    # Modification of first character
    # if convertedString[0] == 'I' and convertedString[1] != ' ':  # "In" can be first word and it should be I as it is
    #     convertedString[0] = 'T'
    if convertedString[0] == '£':
        convertedString[0] = 'I'
    elif convertedString[0] == 'ﬁ':
        convertedString[0] = 'A'
    elif convertedString[0] == '§':
        convertedString[0] = 'S'
    elif convertedString[0] == '?':
        convertedString[0] = 'H'

    return convertedString


def pressString(string):  # takes 1.6 second
    element = 0
    while string[element] is not None:

        # each word typing space
        time.sleep(0.03)
        if 65 <= ord(string[element]) <= 90:  # used shift to write upper alphabets
            kb.press_and_release('shift+' + string[element].lower())
            element += 1
        elif string[element] == '\n':
            kb.press_and_release('\n')
            element += 1
        elif string[element] == '?' or string[element] == '!':  # used shift to write upper symbols
            kb.press_and_release('shift+' + string[element])
            element += 1
        else:
            kb.press_and_release(string[element])
            element += 1


for times in range(0, 5):

    imageToText = screenshotToString()

    modifiedString = convertToFinalString(imageToText)

    print(modifiedString)
    pressString(modifiedString)

    # sleep for sometime, so that new 3 lines get loaded
    time.sleep(0.5)
