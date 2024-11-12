# Python Back-end of AV Simulator

<br>

### Easy Installation

Follow the commands written in `env-prep.sh`. _(Recomemended)_

**Or**

Try run the following command:
```conda env create -f environment.yml```
then activate pyudacity and run:
```pip install -r requirements.txt```

**Or**

Try create conda environment of Python 3.7 then in that environment run:
```pip install -r requirements.txt```

<br>

### Step by Step Guide

1. Create an environment <br/>
```conda create -n pyudacity python=3.7```

2. Activate the environment <br/>
```activate pyudacity```

3. Install jupyter beforehand (since it downgrade the tensorflow version, if it is executed after tensorflow has been installed)<br/>
```conda install -c anaconda jupyter```

4. Install the ipykernel<br/>
```pip install ipykernel```


5. Register your environment<br/>
```python -m ipykernel install --user --name pyudacity --display-name "pyudacity"```

6. Install [tensorflow gpu](https://anaconda.org/anaconda/tensorflow-gpu)<br/>
```conda install -c anaconda tensorflow-gpu```

7. And, finally, install Keras<br/>
```pip install keras```


<br>


### Workflow

This project is divided into three parts:

1) Data Generation.
2) Training the data.
3) Testing.


#### I. Data Generation

In Unity3D simulator environment, we drive the car manually, using keyboard or joystick, and simulataneously, captures the frames or image, using python PIL library through Anaconda’s Spyder, and accessing their associated Steering Angle, Throttle, Velocity, and sending these values and storing it in a CSV file, along with the images.

##### How to do:
1) In "generate_data.py" file, change the directory, where the csv file is going to be saved.
2) In "generate_data.py" file, change the directory, where all your images will be going to be saved.
3) In Unity3D simulator, in Hierarchy, select car, and then in Inspector, under "Car user Control" script, check Generate Data, and uncheck auto_drive Car.<br/>
![car generatecar inspector](https://user-images.githubusercontent.com/31696557/39665840-c4405090-50b7-11e8-9e4f-d74937a0ca8c.png)
4) In Unity3D simulator, in Hierarchy, select Network, in Inspector, active(or check) "Network Data Gen" script, and inactive(uncheck) "Network Con" script.<br/>
![network datagen inspector](https://user-images.githubusercontent.com/31696557/39665856-ff1e5144-50b7-11e8-94e1-97ce57a7fe14.png)
5) Run the simulator in unity3D, then run the program "generate_data.py" from spyder. auto_drive the car manually using keyboard or JoyStick.


<br>

#### II. Train the data

First, the data saved in CSV file is loaded, and image processing is done. In Image processing, the size of the mage is decreased. The actual size was (420, 750) , which was actually very big. It’s size was reduced to (66, 200). Then, the images, and Steering Angle are splitted into training and validation datasets, so that we can use some data for training, and some data for testing.
Then, we apply series of Convolutional Neural Networks on image training datasets, followed by training the model, using Mean Squared Error loss function. This will create several “.h5” files, which we will be used for testing.

##### How to do:
1) Just run the script, "train_cnn.py".


<br>


#### III. Testing

First, image is captured and current steering angle, throttle, and velocity from Unity3D simulator is send over to the socket TCP connection to the Spyder. The image is processed, reducing its size to (66, 200). Then we predict the Steering Angle on the basis of the image, and corresponding throttle value is calculated from the equation. This Steering Angle and Throttle is send back to the Unity3D simulator, and applies to the car, which starts driving by itself. Then again, image is captured, steering angle, throttle, and velocity is send back to the Spyder, and it goes on. It captures the frames(or an image) at 5 frames per seconds.

##### How to do:
1) In "auto_drive.py" file, change the directory, to load the model, which was created by training the data in train_cnn.py.
2) Next, change the directory of "filename", where all current data in a CSV file will be going to be saved.
3) And then, change the directory of "path", where all the current images will be going to be saved.
4) In Unity3D simulator, in Hierarchy, select car, and then in Inspector, under "Car user Control" script, check auto_drive Car, and uncheck Generate Data.<br/>
![car drivecar inspector](https://user-images.githubusercontent.com/31696557/39666518-7f06294a-50c2-11e8-92f8-5ff9fa3b3d04.png)
5) In Unity3D simulator, in Hierarchy, select Network, in Inspector, active(or check) "Network Con" script, and inactive(uncheck)  "Network Data Gen" script.<br/>
![network drivecar inspector](https://user-images.githubusercontent.com/31696557/39666523-a9b2b9ba-50c2-11e8-8c55-45d0b2c3be2e.png)
6) Run the simulator in unity3D, then run the program "auto_drive.py" from spyder. Car will start driving by itself.

<br>


#### Caution!
Before running the codes, make sure you have configured your settings correctly in `config.py`.

<br>


#### Note
1. I used `pip list --format=freeze > requirements.txt` to create `requirement.txt`.
2. I used `conda env export > environment.yml` to create `environment.yml`.


<br>

#### Reference

1. [Self-Driving Simulation](https://github.com/MohammadWasil/Self-Driving-Car-Python)
2. [A Beginner's Guide To Understanding Convolutional Neural Networks](https://adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)
3. [Python requirements file generation](https://blog.csdn.net/qq_36078992/article/details/109435000)
4. [Conda environment file generation](https://blog.csdn.net/shunaoxi2313/article/details/92003710)

<br>
<br>
<br>

By Alexander Ezharjan
4th, April, 2023

