import os
from datetime import datetime
import random

import pytz


def give_time():
    timenow = datetime.now(pytz.timezone('Asia/Colombo')).strftime("%d.%m.%Y %H:%M")
    return timenow

def give_time_delta():
    time_now = datetime.now()
    go_up = datetime(2023,2,12,19,25)
    time_to_go = go_up - time_now
    return f'До прибытия на остров осталось:\nДней: {time_to_go.days}\nЧасов: {int((time_to_go.seconds / 60) / 60)}'

def get_image():
    siski = os.path.abspath(os.path.join("photo"))
    filename = random.choice(os.listdir(siski))
    gif = open(f'{siski}/{filename}', 'rb')
    return gif
