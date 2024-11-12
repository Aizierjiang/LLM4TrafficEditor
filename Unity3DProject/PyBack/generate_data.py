import config as config
import numpy as np
from PIL import ImageGrab
import cv2
import time
import os
import socket

filename = config.cvs_pth 		# change this directory to save your scv file.

firstTime = time.time()

steeringAngle = []
velocity = []
throttle = []

input_image = []
local_address_image = []

# Socket TCP Connection.
host = config.host
port = config.port       # Port number
#data = "1,1,11"         # Data to be send
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP connection
print("starting connection")
try:
    sock.connect((host, port))                  #To connect ot the given port.
    print("Connected")
finally:
    print("Might happen socket is closed!")
#######

path = config.img_pth        # Destination/path to which all the images will be saved
num = 0 

def csv_file(image_dir, steer_Angle, velocity, throttle):
    print("Writing to csv file!")
    f = open(filename, "w")
    f.write("{}, {}, {}, {}\n".format("Image Directory", "Steering Angle", "Current Velocity", "Throttle"))
    for x in zip(image_dir, steer_Angle, velocity, throttle):
        f.write("{}, {}, {}, {}\n".format(x[0], x[1], x[2], x[3]))
    f.close()
    

arr1=[]
arr2=[]
arr3=[]
splitted_data = []
reply=[]
def socketConnection():
    try:
        data = "1,0"
        sock.sendall(data.encode("utf-8"))          # To send the data
        reply = sock.recv(4096).decode("utf-8")    # To receive the data
        print("Actual data received is: ", reply)
        
        splitted_data = reply.split(',')
        print("after splitting the data: ", splitted_data)
        arr1.append(splitted_data[0])
        arr2.append(splitted_data[1])
        arr3.append(splitted_data[2])
        
    except:
        print("Exception:")
    steeringAngle = np.array(arr1) 
    velocity = np.array(arr2)
    throttle = np.array(arr3)
    #csv_file(steeringAngle) this is correct for steering angle.
    return steeringAngle, velocity, throttle

    
local_Address_array = []
while (True):
    num = num + 1
    imageName = 'Image'+ str(num) + '.png'      # Name of the images.
    strAngl, vlcty, thrttl = socketConnection()
    # Try to run the application in full window mode
    printscreen_pil = np.array(ImageGrab.grab(bbox=config.screenshot_area))          # Taking the screenshot and adding in the array
    image_array = []            # TO store our image in an array.
    
    '''
    Storing our image in num py array.
    '''
    image_array.append(printscreen_pil)         
    input_image = np.array(image_array)
    
    # Time to itereate through the loop once.
    print("number ",num)#,"   ",  time.time() - firstTime)
    firstTime = time.time()
    
   
    '''
    for storing the image directory location in our csv file.
    '''
    local_Address_array.append(path+'/'+imageName)          # Append each and every directory to LOcal_address_array
    local_address_image = np.array(local_Address_array)     # and then store it in yet another array.
    csv_file(local_address_image, strAngl, vlcty, thrttl)
      
    
    #cv2.imshow('window', cv2.cvtColor(printscreen_pil, cv2.COLOR_BGR2RGB))          # Displaying the image in a window, and convertng the color BGR to RGB
    cv2.imwrite(os.path.join(path, imageName), printscreen_pil)                                       # Trying to save the image in the exact same directory.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
