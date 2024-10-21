import glob
import imagehash
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tinderbot import TinderBot
from analyze import file
from detect import got
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter as tk
import os
import time
from PIL import Image


def offline():
    my_img_url = file
    my_hash = imagehash.average_hash(Image.open(my_img_url))
    print('Your hash code :- ')
    print(my_hash)

    girls = glob.glob('./offline/*.jpg')

    selected = girls[0]
    accepted_diff = 1000

    for girl in girls:
        girl_hash = imagehash.average_hash(Image.open(girl))
        diff = girl_hash - my_hash
        if diff < accepted_diff:
            selected = girl
            accepted_diff = diff

    print(selected)
    bf_img = Image.open(my_img_url)
    gf_img = Image.open(selected)
    couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
    couple_img.paste(bf_img, (0, 0))
    couple_img.paste(gf_img, (bf_img.width, 0))
    couple_img.show()
    match_hash = imagehash.average_hash(Image.open(selected))
    print('hash code :- ')
    print(match_hash)
