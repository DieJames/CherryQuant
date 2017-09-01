# CherryQuant

Prototype pixel counting software to quant red fluorescence from image files. This counts the total number of red pixels in a image file, thus it should be noted that if multiple experiments are on one image it will contribute to the total pixel count. Crop if neccesary. 
This development version only supports red pixel counting and is developed for windows users. 

Author:  James Gallant, jgallant@sun.ac.za
Company: Stellenbosch University and Vrije Universiteit Amsterdam
version: 1.0
Created: 01/09/2017

Requirements: Python 3, download python at https://www.python.org/downloads/
              Tested on windows 10

Install: 1) Download the tarball and extract in the desired location, the tarball can be deleted. 
         2) Double click on setup.bat. This installs the required libraries, if this does not work follow the instructions below
            2.1) Navigate to command prompt in windows: Search cmd and hit enter
            2.2) Type py and hit enter. This should open python and it should be python 3. 
            2.3) If python is present type exit() to exit python. 
            2.4) Type the following in the windows command prompt: "py -m pip install numpy" (without quotes) and wait for it to finish
            2.5) If numpy has finished type py -m pip install "openCV-python" (without quotes) and wait for it to finish.
          3) The installation is done close the command prompt. 
          
Running the application: 
To run simply double click on the CountPixel.py file. It should automatically initiate python and open a window with a upload button. Click on this button and navigate to the folder containing the files you would like to analyse. Select the folder and CountPixel will start to analyse every file in this directory. 
If it does not initialise a new window right click on CountPixel.py and open with python instead. 

Output:
A text file will be created in the same directory as the image files. Open the text file with excell to access the data. Data can be processed with any standard dataframe and analysis software like graphpad or R. 
