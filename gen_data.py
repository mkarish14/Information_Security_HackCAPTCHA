
#===========================================================================
# Author: Karishma Mehta
# File Name: gen_data.py
# This file reads the image file as input and divides the image into segments of letter
# which are stored in the training folder
#===========================================================================

import numpy as npy
import sys
import os
import cv2
import glob

# constants declaring the size ##########################################################################
MINIMUM_CONTOUR = 40

NEW_IMAGE_WIDTH = 20
NEW_IMAGE_HEIGHT = 30

###################################################################################################
def gen_data(directory, key):

    imgTrainAlphabets = cv2.imread(directory)            					# read in training image
 
    if imgTrainAlphabets is None:                 					        # if problem reading an image
        print "There is an error: image cannot read from file \n\n"        	# print the error message to output
        os.system("Pause")                                  				# pause will help the user to view the message
        return                                              				# exit the program)
    # end if
    imgGrayImage = cv2.cvtColor(imgTrainAlphabets, cv2.COLOR_BGR2GRAY)      # Extract the grayscale image
    imgBlurredImage = cv2.GaussianBlur(imgGrayImage, (5,5), 0)                   # blurr the image 
 

 # Steps to filter image from grayscale to black and white
    imgThreshold = cv2.adaptiveThreshold(imgBlurredImage,                   # input image which is grayscale
                                      255,                                  # 255 is white so make pixels that pass the threshold full white
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # use gaussian to get better results ADAPTIVE_THRESH_GAUSSIAN_C is constant
                                      cv2.THRESH_BINARY_INV,                # inverting makes the foreground to appear white and  background will be black
                                      11,                                   # size of a pixel in the neighborhood which is used to calculate threshold value
                                      2)                                    # constant which is subtracted from the weighted mean
 
 
    imgThresholdCopy = imgThreshold.copy()									# make a copy of imgThreshold into imgThreholdCopy
    numpyContours, numpyHierarchy = cv2.findContours(imgThresholdCopy,          # work on the copy image since the function will modify the original image in finding contours
                                                cv2.RETR_EXTERNAL,          # retrieve the external contours only
                                                cv2.CHAIN_APPROX_SIMPLE)

    numpyFlatImages =  npy.empty((0, NEW_IMAGE_WIDTH * NEW_IMAGE_HEIGHT))

    intClassify = []         										# declare classifications list which will help us to classify our chars 
    image_array = npy.empty((0, NEW_IMAGE_WIDTH * NEW_IMAGE_HEIGHT))
                                    
    intValidCharacters = [ord('a'),ord('b'),ord('c'),ord('d'),ord('e'),ord('f'),ord('g'),ord('h'),ord('i'),ord('j'), #possible characters are from a-z
                     ord('k'),ord('l'),ord('m'),ord('n'),ord('o'),ord('p'),ord('q'),ord('r'),ord('s'),ord('t'),
                     ord('u'),ord('v'),ord('w'),ord('x'),ord('y'),ord('z')]

    for numpyContour in numpyContours:                          	# for each contour portion
        
        if cv2.contourArea(numpyContour) > MINIMUM_CONTOUR:         # if contour is sufficient big to consider
            
            [intX, intY, intW, intH] = cv2.boundingRect(numpyContour)  # get the bounding rectangle specified by intX,intY, intW,intH

														# draw rectangle around 
            cv2.rectangle(imgTrainAlphabets,           	# draw rectangle on original training image
                          (intX, intY),                 # indicates upper left co-ordinates 
                          (intX+intW,intY+intH),        # indicates lower right co-ordinates
                          (0, 0, 255),                  # the RGB color code for red
                          2)                            # thickness of the bounded Rectangle

            imgROImage = imgThreshold[intY:intY+intH, intX:intX+intW]                                  # crop char out of threshold image
            imgROIResized = cv2.resize(imgROImage, (NEW_IMAGE_WIDTH, NEW_IMAGE_HEIGHT))     # resizes the image which will aid in storing it

            cv2.imshow("imgROI", imgROImage)                    # displays the cropped out char
            cv2.imshow("imgROIResized", imgROIResized)      # displays the resized image 
            
            cv2.imshow(directory, imgTrainAlphabets)      # show training numbers image, this will now have red rectangles drawn on it

            intCharacter = key_pressed
            if intCharacter == 27:                   # check if Esc key is pressed
                sys.exit()                      	 # exit the program
            elif intCharacter in intValidCharacters:      # else if the character is int valid charater list 
                intClassify.append(ord(chr(intCharacter)))                                                # append method is used to append classification char to integer  
                numpyFlattenedImage = imgROIResized.reshape((1, NEW_IMAGE_WIDTH * NEW_IMAGE_HEIGHT))  # used to flatten image to 1 dimensional numpy array 
                numpyFlatImages = npy.append(numpyFlatImages, numpyFlattenedImage, 0)                    # add current flattened numpy array image to list 
                image_array = npy.append(image_array, numpyFlattenedImage, 0) 
            # end if
        # end if
    # end for
    flatClassify = np.array(intClassify, np.float32)                   # convert classifications list into numpy array of floats
    numpyClassify = flatClassify.reshape((flatClassify.size, 1))   # numpy array of floats to 1 dimensional to write to file later
    label = flatClassify.reshape((flatClassify.size, 1))
   
	file1=open('label.txt','a')
    file2=open('image_arr.txt','a')
    npy.savetxt(file1, label)
    npy.savetxt(file2, image_array)
    file1.close()
    file2.close()
    #print "training complete"
    
    cv2.destroyAllWindows()             # remove windows from memory

    return



if __name__ == "__main__":
    file1=open('label.txt','w')
    file2=open('image_arr.txt','w')
    file1.write("")
    file2.write("")
    file1.close()
    file2.close()
    array_folder = ["training/a/*.png","training/b/*.png","training/c/*.png","training/d/*.png","training/e/*.png",
               "training/f/*.png","training/g/*.png","training/h/*.png","training/i/*.png","training/k/*.png",
               "training/l/*.png","training/m/*.png","training/n/*.png","training/o/*.png","training/p/*.png",
               "training/r/*.png","training/s/*.png","training/t/*.png","training/u/*.png","training/v/*.png",
               "training/w/*.png","training/x/*.png","training/y/*.png","training/z/*.png"]
    for item in array_folder:
        files = glob.glob(item)
        for file in files:
            gen_data(file, ord(item.split("/")[1]))
    print "training complete"


