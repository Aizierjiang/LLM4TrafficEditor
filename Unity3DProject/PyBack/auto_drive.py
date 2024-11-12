import config as config
import socket

from keras.models import load_model


from PIL import ImageGrab
import numpy as np
import cv2
import os

#Load the model.
model = load_model(config.model_pth) 	# Directory to load the model


# Socket TCP Connection.
host = config.host
port = config.port            # Port number
#data = "1,1,11"         # Data to be send
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP connection
print("starting connection")
try:
    sock.connect((host, port))                  #To connect ot the given port.
    print("Connected")
    
except:
    print("Might happen socket is closed!")
#######

def send_data(steering_angle, throttle):
    data_01 = str(steering_angle)
    data_02 = str(throttle)
    data = data_01 + ',' + data_02
    sock.sendall(data.encode("utf-8"))          # To send the data

steeringAngleList = []
velocityList = []
throttleList = []

steeringAngle = 0
velocity = 0
throttle = 0

arr1=[]
arr2=[]
arr3=[]
splitted_data = []
reply=[]
def socketConnection():
    global globalsteeringAngle
    global velocity
    global throttle
    try:
        reply = sock.recv(2048).decode("utf-8")    # To receive the data
        #print("Actual data received is: ", reply)
       
        splitted_data = reply.split(',')
        #print("after splitting the data: ", splitted_data)
        arr1.append(splitted_data[0])
        arr2.append(splitted_data[1])
        arr3.append(splitted_data[2])
        
        steeringAngle = float(splitted_data[0])
        velocity = float(splitted_data[1])
        throttle = float(splitted_data[2])
        
    except Exception as e:
        print("Exception:", e)
    
    steeringAngleList = np.array(arr1) 
    velocityList = np.array(arr2)
    throttleList = np.array(arr3)

    return steeringAngleList, velocityList, throttleList, steeringAngle, velocity, throttle


filename = config.cvs_pth 	#Directory to save your current Data in a csv file.

def csv_file(steer_Angle, velocity, throttle):
    
    #print("Writing to csv file!")
    f = open(filename, "w")
    f.write("{},{},{}\n".format("Steering Angle", "Current Velocity", "Throttle"))
    
    for x in zip( steer_Angle, velocity, throttle):
        f.write("{},{},{}\n".format(x[0], x[1], x[2]))
    
    f.close()

#############################   
# MAX_SPEED = 25
MAX_SPEED = 100
MIN_SPEED = 10
speed_limit = MAX_SPEED

def preprocess(image):
    return cv2.resize(image, (200, 66), cv2.INTER_AREA)


def drive(image, steering_angle, velocity, throttle):

    try:
        image = np.asarray(image)       # from PIL image to numpy array
        image = preprocess(image)       # apply the preprocessing
        image = np.array([image])       # the model expects 4D array
        
        steering_angle = float(model.predict(image, batch_size=1))
        steering_angle = (steering_angle/10)
        global speed_limit
        if velocity > speed_limit:
            speed_limit = MIN_SPEED  # slow down
        else:
            speed_limit = MAX_SPEED
        throttle = 1.0 - steering_angle**2 - (velocity/speed_limit)**2

        print('{} {} {}'.format(steering_angle, throttle, velocity))
        steering_angle = (steering_angle*10)
        send_data(steering_angle, throttle)
        
    except Exception as e:
        print("Exception:", e)
 
num = 0  
path = config.img_pth         # Destination/path to which all the current images will be saved 
while (True):
    num = num + 1
    imageName = 'auto'+ str(num) + '.png'      # Name of the images.
    #collecting current data
    strAngl, vlcty, thrttl, steeringAngle, velocity, throttle  = socketConnection()
    image = np.array(ImageGrab.grab(bbox=config.screenshot_area))          # Taking the screenshot and adding in the array
    
    csv_file(strAngl, vlcty, thrttl)
    cv2.imwrite(os.path.join(path, imageName), image)                                       # Trying to save the image in the exact same directory.
    

    drive(image, steeringAngle, velocity, throttle)

"""
### NOTE: divide steering angle by 10.
"""