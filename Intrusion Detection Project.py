import cv2
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)
import tkinter as tk
from tkinter import simpledialog
import datetime
import random




print("Welcome To Super_Nova System")

#simpledialog.askstring(title="Test",prompt="Welcome to SUPERNOVA Systems")

ROOT = tk.Tk()

ROOT.withdraw()



USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:-")
print("Hello",USER_INP)

#USER_password = simpledialog.askstring(title="Test",
  #                                prompt="Please Enter your password:-")


#User_name = str(input("Please Enter your User name"))

#print("Enter only numerci")
Pass_word= "123456"

Attempt = (0, 1, 2)
x=int (2) 
#i=int(input("Enter Your Password : "))
USER_password = simpledialog.askstring(title="Test",
                                  prompt="Please Enter your password:-")




for z in range(0,3) :
      if (USER_password==Pass_word):
            print("Thank you for logging in system")
            break
      else :
      #print("You have only 3 attept")
        print("\nThe password was wrong...\nPlease Enter the Right one...")
        print("Attempts Remaining only ",x)
   #     print("Your password is-", USER_password)
        
        x=x-1
      if (x>=0) :
           # i=int(input("Enter Your Password again: "))
           USER_password = simpledialog.askstring(title="Test",
                                  prompt="Please Enter your password:-")
           

if(x==-1):
    
    
    # for camera initialise
    cam_port = 0
    cam = VideoCapture(cam_port)
    
    # reading the input using the camera
    result, image = cam.read()
    if result:
    
        # Here we give frame name t
        imshow("Frame", image)
    
        # saving in local directory
        imwrite("Frame.png", image)
    
        #this is use for destroy window
        waitKey(0)
        print("\n")
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print("\n")

        location=("Sunderdeep","Hapur","Dasna","Noida","Pilkhuwa")
        # Random_loaction=random.location()
        Random_location=random.choice(location)
        print("Location:- ",Random_location)
        Time= datetime.datetime.now()
        print("Current Date & Time:-",Time)

        print("\n")
                
    
    # This part is execued when capture image corrupted
    else:
        print("No image detected. Please! try again")

































