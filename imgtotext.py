import pyautogui as pg
import time
import pytesseract
from PIL import Image
import re

def screen(i):

    path = f'fina2143adavery eye turn oil near j{i}.png'
    pg.screenshot(path,region=(470,270 ,950, 100))
    return path
def run():
    i = 0
    while True:

        x = (pytesseract.image_to_string(Image.open(screen(i)),lang='pol'))
        y = re.sub(r'\n\s*\n', '\n', x, flags=re.MULTILINE)
        z = y.replace('\n',' ')
        pg.write(z, interval=0.01)
        print(z)
        time.sleep(1)
        i += 1

time.sleep(5)
run()
