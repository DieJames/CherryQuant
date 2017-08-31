#!/usr/bin/env python



import os, os.path
import cv2
import numpy as np
import os
from tkinter import *
from tkinter import filedialog


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("CountPixel")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        uploadButton = Button(self, text="Upload", command=self.client_upload, width=15)

        # placing the button on my window
        uploadButton.place(x=100, y=25)




    def client_upload(self):
        imageDir = filedialog.askdirectory(initialdir="/",  title='Please select a directory')
        print(imageDir)
        out = open(imageDir + "/resutls.txt", "w")
        header = 'sample' + '\t' + "pixels"
        out.write(header + '\n')
        image_path_list = []
        valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]  # specify your vald extensions here
        valid_image_extensions = [item.lower() for item in valid_image_extensions]

        for file in os.listdir(imageDir):
            extension = os.path.splitext(file)[1]
            if extension.lower() not in valid_image_extensions:
                continue
            image_path_list.append(os.path.join(imageDir, file))

        # loop through image_path_list to open each image
        for imagePath in image_path_list:
            # print(imagePath)
            image_name = os.path.basename(imagePath)
            print(image_name)

            img = cv2.imread(imagePath)

            RED_MIN = np.array([0, 0, 51], np.uint8)
            RED_MAX = np.array([50, 50, 255], np.uint8)

            dst = cv2.inRange(img, RED_MIN, RED_MAX)
            no_red = cv2.countNonZero(dst)
            print(str(no_red))

            # writing outputs here
            out_results = image_name + '\t' + str(no_red)
            out.write(out_results + '\n')

        out.close()
        exit()

root = Tk()

#size of the window
root.geometry("300x50")

app = Window(root)



root.mainloop()

#imageDir = input('input directory with images: ') #specify your path here
