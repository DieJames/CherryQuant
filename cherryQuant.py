#!/usr/bin/env python



import os, os.path
import cv2
import numpy as np
import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar


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
        global cherryButton
        cherryButton = Button(self, text="RFP",  command=self.client_cherry, widt=15)
        #gfpButton = Button(self, text="GFP", command=self.client_gfp)
        global gfpButton
        gfpButton = Button(self, text="GFP", command=self.client_gfp, width=15)

        global uploadButton
        uploadButton = Button(self, text="Upload", command=self.client_upload, width=15)
        runButton = Button(self, text="run", command=self.client_run, width=10)

        # placing the button on my window
        cherryButton.place(x=30, y=70)
        gfpButton.place(x=30, y=115)
        uploadButton.place(x=30, y=25)
        runButton.place(x=300, y=160)

    def client_upload(self):
        imageDir = filedialog.askdirectory(initialdir="/",  title='Please select a directory')
        print(imageDir)
        global out
        out = open(imageDir + "/results.txt", "w")
        header = 'sample' + '\t' + "pixels"
        out.write(header + '\n')
        global image_path_list
        image_path_list = []
        valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]  # specify your vald extensions here
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
        global cherry
        cherry = "True"
        if cherry == "True":
           cherryButton.configure(backgroun="red", fg="white", text="ready")
           global gfp
           gfp = "False"
           if gfp == "False":
               gfpButton.configure(background=orig_colour, fg="black", text="GFP")




    def client_gfp(self):
        global gfp
        gfp = "True"
        if gfp == "True":
            gfpButton.configure(background="green", fg="white", text="ready")
            global cherry
            cherry = "False"
            if cherry == "False":
                cherryButton.configure(background=orig_colour, fg="black", text="RFP")





    #client upload is for directory uploading and at the moment runs the full script. adding more buttons and subset
    #here is a possibility

        # loop through image_path_list to open each image


    # function to run the script
    def client_run(self):
        progressbar = Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
        progressbar.pack(side="bottom")
        progressbar.start()
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

            if gfp == "True":
                GREEN_MIN = np.array(([0, 51, 0]))
                GREEN_MAX = np.array([50, 255, 50])

                dst_g = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
                no_green = cv2.countNonZero(dst_g)
                print(str(no_green))
                out_results = image_name + '\t' + str(no_green)

            # writing outputs here

            out.write(out_results + '\n')

        out.close()
        progressbar.stop()
        exit()

root = Tk()


#size of the window
root.geometry("400x200")

app = Window(root)



root.mainloop()

#imageDir = input('input directory with images: ') #specify your path here
