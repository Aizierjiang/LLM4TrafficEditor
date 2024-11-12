import config as config
import pandas as p
import cv2
from sklearn import model_selection
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Lambda, Conv2D
from keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from PIL import Image
import numpy as np

image_input_array = []

def LoadData():  
    image_input_array2 = np.zeros((config.img_count, 66, 200,3))         
    URL = config.cvs_pth		     # Load your csv file.
    
    data = p.read_csv(URL)
    
    image_input = data['Image Directory']
    steering_Angle = data[' Steering Angle'].values
    
    for i in range(0,len(image_input)):
        print("Processing image: ", i)
        
        URL_image = image_input[i]
        image_input_array = Image.open(URL_image)
        image_input_list = np.array(image_input_array)         
        print(image_input_list.shape)           
        
        image_input_list2 = cv2.resize(image_input_list, dsize=(200, 66), interpolation=cv2.INTER_CUBIC)
        print(image_input_list2.shape)
        
        image_input_list2 = np.expand_dims(image_input_list2, axis=0)
        print(image_input_list2.shape)      
        print(len(image_input_list2))
        
        image_input_array2[i, :, :, :] = image_input_list2
        print(image_input_array2.shape)
        print(len(image_input_array2))
    
    print("Processed image successfully!")
    print(image_input_array2.shape)
    
    validation_size = 0.20          # validation is 0.20, so the size of the X and Y validaion will be 20% of the X and Y(actual size of the array)
    seed = 7
    
    # This splits the dataset, so that we can use some data for training, some for testing.
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(image_input_array2, steering_Angle, test_size=validation_size, random_state=seed)

  	# If the actual image and steering data is 2116, then...    
    print(X_train.shape)         # the Size is 1692 which is about 80% of actual image data.         1692/2116 * 100 = 79.9621% ~ 80%
    print(Y_train.shape)         # the size is 1692 which is about 80% of actual steering data.      1692/2116 * 100 = 79.9621% ~ 80%
    print(X_validation.shape)    # the size is 424 which is about 20% of actual image data.          424/2116 * 100 = 20.0378% ~ 20%
    print(Y_validation.shape)    # the size is 424 which is about 20% of actual steering data.       424/2116 * 100 = 20.0378% ~ 20%
    
    return X_train, X_validation, Y_train, Y_validation

def buildModel(image_train):
    #print("building our model")
    model = Sequential()
    model.add(Lambda(lambda x : x/127.5-1.0, input_shape = (66,200,3)))
    model.add(Conv2D(24, (5, 5), activation = "elu", strides=(2,2)))
    model.add(Conv2D(36, (5, 5), activation = "elu", strides=(2,2)))
    model.add(Conv2D(48, (5, 5), activation = "elu", strides=(2,2)))
    model.add(Conv2D(64, (5, 5), activation = "elu"))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(100, activation='elu'))
    model.add(Dense(50, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(1, activation='elu'))
    model.summary()
    
    return model

def train(model, image_train, image_valiation, steer_train, steer_validation):
    checkpoints = ModelCheckpoint('./model/data-{epoch:03d}.h5', monitor='val_loss', verbose=0, save_best_only=True, mode='auto')    # You can change the name of the model, by replacing "data" with your preferred name.
    
    model.compile(loss='mean_squared_error', optimizer=Adam(lr = 0.001))
    
    model.fit(image_train, steer_train, epochs=60, callbacks=[checkpoints],validation_data=(image_valiation, steer_validation))
        
image_train, image_valiation, steer_train, steer_validation = LoadData()
model = buildModel(image_train)
train(model, image_train, image_valiation, steer_train, steer_validation)


