import requests
from bs4 import BeautifulSoup as bs
import random

r = requests.get('https://create.vista.com/ru/photos/%D0%A8%D1%80%D0%B8-%D0%9B%D0%B0%D0%BD%D0%BA%D0%B0/')

text = r.text

soup = bs(text, "html.parser")

theresult = {}

def parser():
    i = 0
    for qwerty in soup.find_all('img'):
        theresult[i] = qwerty.get('src')
        print(theresult[i])
        i = i + 1
        print(i)
    i = random.randint(1, 19)
    print(theresult[i])


parser()