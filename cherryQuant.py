#!/usr/bin/env python
import os, os.path
import cv2
import numpy as np
import os
from tkinter import *
from tkinter import filedialog

import time


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("cherryQuant")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating button instances
        global uploadButton
        uploadButton = Button(self, text="Upload", command=self.client_upload, width=15)
        global cherryButton
        cherryButton = Button(self, text="Quant red",  command=self.client_cherry, widt=15)
        #gfpButton = Button(self, text="GFP", command=self.client_gfp)
        global gfpButton
        gfpButton = Button(self, text="Quant green", command=self.client_gfp, width=15)
        global bfpButton
        bfpButton = Button(self, text="Quant blue", command=self.client_bfp, width=15)
        runButton = Button(self, text="Submit", command=self.client_run, width=10)
        global CustomRangeButton
        CustomRangeButton = Button(self, text="Choose RGB range", command=self.client_custom, width=15)



        # placing the button on my window
        cherryButton.place(x=30, y=70)
        gfpButton.place(x=30, y=115)
        bfpButton.place(x=30, y=160)
        uploadButton.place(x=30, y=25)
        CustomRangeButton.place(x=265, y=5)
        runButton.place(x=315, y=160)



    def client_upload(self):
        global BEGIN
        BEGIN = "True"
        global imageDir
        imageDir = filedialog.askdirectory(initialdir="/",  title='Please select a directory')
        print(imageDir)

        global image_path_list
        image_path_list = []
        valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]  # specify your valid extensions here
        valid_image_extensions = [item.lower() for item in valid_image_extensions]

        for file in os.listdir(imageDir):
            extension = os.path.splitext(file)[1]
            if extension.lower() not in valid_image_extensions:
                continue
            image_path_list.append(os.path.join(imageDir, file))

        global orig_colour
        orig_colour = uploadButton.cget("background")
        uploadButton.configure(text="Ready")

    #mcerry analysis
    def client_cherry(self):
        if BEGIN == "True":
            global cherry
            cherry = "True"
            if cherry == "True":
                cherryButton.configure(backgroun="red", fg="white", text="Ready")

                global gfp
                gfp = "False"
                if gfp == "False":
                    gfpButton.configure(background=orig_colour, fg="black", text="Quant green")

                global bfp
                bfp = "False"
                if bfp == "False":
                    bfpButton.configure(background=orig_colour, fg="black", text="Quant blue")

                global custom
                custom = "False"


    def client_gfp(self):
        if BEGIN == "True":
            global gfp
            gfp = "True"
            if gfp == "True":
                gfpButton.configure(background="green", fg="white", text="Ready")

                global cherry
                cherry = "False"
                if cherry == "False":
                    cherryButton.configure(background=orig_colour, fg="black", text="Quant red")

                global bfp
                bfp = "False"
                if bfp == "False":
                    bfpButton.configure(background=orig_colour, fg="black", text="Quant blue")

                global custom
                custom = "False"

    def client_bfp(self):
        if BEGIN == "True":
            global bfp
            bfp = "True"
            if bfp == "True":
                bfpButton.configure(background="Blue", fg="white", text="Ready")

                global cherry
                cherry = "False"
                if cherry == "False":
                    cherryButton.configure(background=orig_colour, fg="black", text="Quant red")

                global gfp
                gfp = "False"
                if gfp == "False":
                    gfpButton.configure(background=orig_colour, fg="black", text="Quant green")

                global custom
                custom = "False"



    def client_custom(self):
        global custom
        custom = "True"
        if custom == "True":
            global cherry
            cherry = "False"
            if cherry == "False":
                cherryButton.configure(background=orig_colour, fg="black", text="Quant red", state="disabled")
            global gfp
            gfp = "False"
            if gfp == "False":
                gfpButton.configure(background=orig_colour, fg="black", text="Quant green", state="disabled")
            global bfp
            bfp = "False"
            if bfp == "False":
                bfpButton.configure(background=orig_colour, fg="black", text="Quant blue", state="disabled")
            # user input e1 = Minimum RGB entry

            global e1_lab
            global e1_labR
            global e1_labG
            global e1_labB
            global entry_R_min
            global entry_G_min
            global entry_B_min
            global entry_R_max
            global entry_G_max
            global entry_B_max
            global e2_lab
            global usr_R_min
            global usr_R_max
            global usr_G_min
            global usr_G_max
            global usr_B_min
            global usr_B_max

            e1_lab = Label(self, text="Minimum RGB value")
            e1_lab.place(x=175, y=50)

            e1_labR = Label(self, text="R")
            e1_labR.place(x=305, y=35)


            usr_R_min = StringVar()
            entry_R_min = Entry(self, textvariable=usr_R_min)
            entry_R_min.place(x=300, y=55, width=25)

            e1_labG = Label(self, text="G")
            e1_labG.place(x=335, y=35)

            usr_G_min = StringVar()
            entry_G_min = Entry(self, textvariable=usr_G_min)
            entry_G_min.place(x=330, y=55, width=25)

            e1_labB = Label(self, text="B")
            e1_labB.place(x=366, y=35)

            usr_B_min = StringVar()
            entry_B_min = Entry(self, textvariable=usr_B_min)
            entry_B_min.place(x=360, y=55, width=25)

            e2_lab = Label(self, text="Maximum RGB value")
            e2_lab.place(x=175, y=85)

            usr_R_max = StringVar()
            entry_R_max = Entry(self, textvariable=usr_R_max)
            entry_R_max.place(x=300, y=85, width=25)

            usr_G_max = StringVar()
            entry_G_max = Entry(self, textvariable=usr_G_max)
            entry_G_max.place(x=330, y=85, width=25)

            usr_B_max = StringVar()
            entry_B_max = Entry(self, textvariable=usr_B_max)
            entry_B_max.place(x=360, y=85, width=25)

            global CancelButton
            CancelButton = Button(self, text="Cancel", width=7, command=self.client_cancel)
            CancelButton.place(x=330, y=120)

            global OkButton
            OkButton = Button(self, text="Ok", command=self.client_ok, width=7)
            OkButton.place(x=260, y=120)


    def client_cancel(self):
        Cancel = "True"
        if Cancel == "True":
            e1_lab.destroy()
            e1_labR.destroy()
            e1_labB.destroy()
            e1_labG.destroy()
            entry_R_min.destroy()
            entry_R_max.destroy()
            entry_G_min.destroy()
            entry_G_max.destroy()
            entry_B_min.destroy()
            entry_B_max.destroy()
            e2_lab.destroy()
            OkButton.destroy()
            CancelButton.destroy()
            cherryButton.configure(background=orig_colour, fg="black", text="Quant red", state="normal")
            gfpButton.configure(background=orig_colour, fg="black", text="Quant green", state="normal")
            bfpButton.configure(background=orig_colour, fg="black", text="Quant blue", state="normal")


        CustomRangeButton = Button(self, text="Choose RGB range", command=self.client_custom, width=15)
        CustomRangeButton.place(x=265, y=5)
        global custom
        custom = "True"

    def client_ok(selfs):
        global custom
        global minRedVal
        global maxRedVal
        global minGreenVal
        global maxGreenVal
        global minBlueVal
        global maxBlueVal
        custom = "True"
        minRedVal = usr_R_min.get()
        maxRedVal = usr_R_max.get()
        minGreenVal = usr_G_min.get()
        maxGreenVal = usr_G_max.get()
        minBlueVal = usr_B_min.get()
        maxBlueVal = usr_B_max.get()

        entry_R_max.configure(state="disabled")
        entry_R_min.configure(state="disabled")
        entry_G_max.configure(state="disabled")
        entry_G_min.configure(state="disabled")
        entry_B_min.configure(state="disabled")
        entry_B_max.configure(state="disabled")

        OkButton.configure(text="Ready")
    # function to run the script
    def client_run(self):
        start = time.clock()
        global custom
        global cherry
        global gfp
        global bfp
        out = open(imageDir + "/results.txt", "w")

        if cherry == "True":
            header = 'Sample' + '\t' + 'Red pixel count'
            out.write(header + '\n')

        if gfp == "True":
            header = 'Sample' + '\t' + 'Green pixel count'
            out.write(header + '\n')

        if bfp == "True":
            header = 'Sample' + '\t' + 'Blue pixel count'
            out.write(header + '\n')

        #global custom
        if custom == "True":
            header = 'Sample' + '\t' + 'Custom pixel range'
            out.write(header + '\n')

        for imagePath in image_path_list:
            # print(imagePath)
            image_name = os.path.basename(imagePath)
            print(image_name)
             #cv2 is BGR
            img = cv2.imread(imagePath)
            if cherry == "True":
                RED_MIN = np.array([0, 0, 51], np.uint8)
                RED_MAX = np.array([50, 50, 255], np.uint8)

                dst = cv2.inRange(img, RED_MIN, RED_MAX)
                no_red = cv2.countNonZero(dst)
                print(str(no_red))
                out_results = image_name + '\t' + str(no_red)
                out.write(out_results + '\n')

            if gfp == "True":
                GREEN_MIN = np.array(([0, 51, 0]))
                GREEN_MAX = np.array([50, 255, 50])

                dst_g = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
                no_green = cv2.countNonZero(dst_g)
                print(str(no_green))
                out_results = image_name + '\t' + str(no_green)
                out.write(out_results + '\n')

            if bfp == "True":
                BLUE_MIN = np.array([51, 0, 0])
                BLUE_MAX = np.array([255, 50, 50])
                dst_b = cv2.inRange(img, BLUE_MIN, BLUE_MAX)
                no_blue = cv2.countNonZero(dst_b)
                print(str(no_blue))
                out_results = image_name + '\t' + str(no_blue)
                out.write(out_results + '\n')

            if custom == "True":
                matr_min = np.matrix('%s; %s; %s' % (minBlueVal, minGreenVal, minRedVal))
                matr_max = np.matrix('%s; %s; %s' % (maxBlueVal, maxGreenVal, maxRedVal))
                print(matr_min)
                CUSTOM_MIN = np.array(matr_min)
                CUSTOM_MAX = np.array(matr_max)
                dst_c = cv2.inRange(img, CUSTOM_MIN, CUSTOM_MAX)
                no_custom = cv2.countNonZero(dst_c)
                print(str(no_custom))
                out_results = image_name + '\t' + str(no_custom)
                out.write(out_results + '\n')
            # writing outputs here


        out.close()
        print("Total run time for selected samples in seconds was...")
        print(time.clock() - start)
        exit()

root = Tk()
#size of the window
root.geometry("400x200")
app = Window(root)
root.mainloop()