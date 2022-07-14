import pyautogui as pg
import time
import pytesseract
from PIL import Image

time.sleep(3)
print(pytesseract.image_to_string(Image.open('rozp.png')))

file = open("animals.txt",'r')
#y = pg.locateCenterOnScreen('Znajdz3.png')
#pg.click(y)
"""pg.write("Myslisz ze to takie latwe?",interval =0.1)
pg.press('Enter')
pg.write("To pa tera",interval =0.1)"""

"""a = pg.prompt('radio')
if a == "radio":"""
pg.click(30,70)
time.sleep(1)
z = pg.locateCenterOnScreen('Znajdz4.png')
pg.click(z)
time.sleep(2)
v = pg.locateCenterOnScreen('szukaj1.png')
pg.click(v)
pg.write("eska mix 2022", interval=0.1)
pg.press('Enter')
time.sleep(2)
pg.click(pg.locateCenterOnScreen('szukaj4.png'))
time.sleep(2)
pg.click(500,400)
"""
if a == 'Szymon':
    for i in range(5):
        pg.alert(text="Fatal error 404",title='Windows Update',button='OK')
    y = pg.locateCenterOnScreen('Znajdz3.png')
    pg.click(y)
    for i in file:
        pg.write(f'Syzdek to {i}!')
        pg.press('Enter')
"""