import imageio
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL.ExifTags import TAGS
import cv2
import webbrowser

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow("test")


img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "./boys/opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

Tk().withdraw()
file = tk.StringVar()
file = askopenfilename(initialdir=file, filetypes=[("jpg files", "*.jpg")])
print(file)

pic = imageio.imread(file)


# def img_values():
#     print('Type of the image : ', type(pic))
#     print('Shape of the image : {}'.format(pic.shape))
#     print('Image Height {}'.format(pic.shape[0]))
#     print('Image Width {}'.format(pic.shape[1]))
#     print('Dimension of Image {}'.format(pic.ndim))
#     print('Image size {}'.format(pic.size))
#     print('Maximum RGB value in this image {}'.format(pic.max()))
#     print('Minimum RGB value in this image {}'.format(pic.min()))
#     type(pic)
#     format(pic.shape)
#     format(pic.shape[0])
#     format(pic.shape[1])
#     format(pic.ndim)
#     format(pic.size)
#     format(pic.max())
#     format(pic.min())


def dotty():
    filo = open('imageproperties.txt', "w")
    text = ('Type of the image : \n', type(pic))
    text1 = ('Shape of the image : {} \n'.format(pic.shape))
    text2 = ('Image Height {} \n'.format(pic.shape[0]))
    text3 = ('Image Width {} \n'.format(pic.shape[1]))
    text4 = ('Dimension of Image {} \n'.format(pic.ndim))
    text5 = ('Image size {} \n'.format(pic.size))
    text6 = ('Maximum RGB value in this image {} \n'.format(pic.max()))
    text7 = ('Minimum RGB value in this image {} \n'.format(pic.min()))
    filo.writelines(str(text))
    filo.writelines(str(text1))
    filo.writelines(str(text2))
    filo.writelines(str(text3))
    filo.writelines(str(text4))
    filo.writelines(str(text5))
    filo.writelines(str(text6))
    filo.writelines(str(text7))

    webbrowser.open("imageproperties.txt")

    image = Image.open(file)
    exifdata = image.getexif()

    for tagid in exifdata:
        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        # passing the tagid to get its respective value
        value = exifdata.get(tagid)

        # printing the final result
        text8 = f"{tagname:25}: {value}"

        filo.writelines(str(text8))



def image_analysis():
    #print('IMAGE ANALYSIS?-y/n')
    #if 'y' in input():

    plt.title('Your Image')
    plt.figure(figsize=(5, 5))
    plt.imshow(pic)
    #plt.show()

    for c in zip(range(3)):
        split_img = np.zeros(pic.shape, dtype="uint8")
        split_img[0:255, :, c] = pic[:, :, c]
        plt.figure(figsize=(5, 5))
        plt.imshow(split_img)

    #plt.show()

    return plt.show()


def rgb_channel():

    for c in zip(range(3)):
        split_img = pic[:, :, c]
        plt.ylabel('Height {}'.format(pic.shape[0]))
        plt.xlabel('Width {}'.format(pic.shape[1]))
        plt.figure(figsize=(5, 5))
        plt.imshow(split_img)
    return plt.show()
