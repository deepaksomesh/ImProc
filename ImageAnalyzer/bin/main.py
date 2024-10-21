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
from dependencies import dpp
import time
from PIL import Image




#img = image_analysis()

#get = got()

print('\nyour image looks great\n' or '\nImage looks better\n' or '\nWe are good go further\n')

#def matching():
    #print('Your hash code :- ')
    #print(my_hash)
    #print('MATCH IMAGES ONLINE OR OFFLINE- o/f')


my_img_url = file
my_hash = imagehash.average_hash(Image.open(my_img_url))


def online():
    my_img_url = file
    my_hash = imagehash.average_hash(Image.open(my_img_url))
    print('Your hash code :- ')
    print(my_hash)
    entered = given.get()
    chdriver = webdriver.Chrome('./chrome/chromedriver.exe')
    chdriver.get('https://www.google.co.in/imghp?hl=en&ogbl')
    searchbox = chdriver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    searchbox.send_keys('potraits of ' + entered)
    searchbox.send_keys(Keys.ENTER)




    resultpage = chdriver.execute_script('return document.body.scrollHeight')
    while True:
        chdriver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        newpage = chdriver.execute_script('return document.body.scrollHeight')
        try:
            chdriver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if newpage == resultpage:
            break
        resultpage = newpage
    # Tk().withdraw()
    # dile = tk.StringVar()
    # dile = askdirectory()
    for i in range(0, 50):
        try:
            chdriver.find_element_by_xpath(
                '//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').screenshot(
                './downloads/images/girl (' + str(i) + ').png')
        except:
            pass

    girls = glob.glob('./downloads/images/*.png')

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


given = tk.Entry(dpp, highlightthickness=2)
given.config(highlightbackground='#b1cbde', highlightcolor='#b1cbde')
given.pack(anchor=CENTER)








#




#print('\nWANT TO MATCH IMAGES ON ONLINE SITE?-y/n')
#if 'y' in input():
 #   bot = TinderBot()
  #  bot.login()

