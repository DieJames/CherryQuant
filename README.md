# CherryQuant

Prototype pixel counting software to quant red fluorescence from image files. This software quantifies the **total** flourescence intensity within image files. cherryQuant supports default RGB channels of red, green and blue as well as an option for a custom RGB range.

## Requirements 
Python 3, download python [here](https://www.python.org/downloads/)
 This software was tested on windows 10
 
 ## installation
 
1. Download the tarball and extract in the desired location, the tarball can be deleted. 
2. Double click on setup.bat. This installs the required libraries, if this does not work follow the instructions below
   2.1. Navigate to command prompt in windows: Search cmd and hit enter
   
   2.2. Type py and hit enter. This should open python and it should be python 3. 
   2.3. If python is present type exit() to exit python. 
   2.4. Type the following in the windows command prompt 
   ```
   py -m pip install numpy  
   py -m pip install openCV-python
   
   ``` 
 3. The installation is done close the command prompt. 
          
## Running the application: 

To run simply double click on the CountPixel.py file. It should automatically initiate python and open a window with a upload button. Some problems occur if both python 2 and python 3 is installed. If this is the case open the command prompt and type 
```
py-3 cherryQuant.py
```
## Output:

A text file will be created in the same directory as the image files. Open the text file with excell to access the data. Data can be processed with any standard dataframe and analysis software like graphpad or R. 

## testing the software

Unzip the test folder to test/. Initiate cherryQuant and choose one of the default fluorescence channels. Run the software and inspect the output. 
