# Traffic Editor

This is a traffic editor for research purpose of autonomous driving and smart transportation.


<br>
<br>
<br>


## Keyboard shortcuts

1. `Shift + F12` : Change scene to different modes.
2. `Shift + O`   : Restore car's original position to avoid being stuck.
3. `Ctrl + K`    : Change camera to view from different angle, note that there are 4 different controllable views. (Only available in "Autonomous" "Train" modes.)
4. `Backspace`   : Show or hide Weather System's UI.
5. `Esc`         : Quit application.
6. `K`           : Undo line draw, only in `RoadEditor`.




<br>
<br>
<br>



## Introduction
1. ThirdPerson in the scene can be controlled by the TCP connection to the `UDPPort` settings in configuration file.
2. Move the ThirdPerson to a position: Send `P:float xPos, float yPos, float angle` formatted message to teh server, eg: `P:1,2,3`.
4. Continue to move the ThirdPerson to a direction: Send `MP:int verticalDir, int horizontalDir` formatted message to teh server, eg: `MP:1,1`.
5. In AI controlling scenes, the `human server` for controlling Metahuman is turned off so that you can control the Metahuman manually faster. 
6. In AI controlling scenes, turn on the `human server` by clicking the button on the screen then you are able to control the Metahuman remotely using TCP connection mentioned above.
7. In AI controlling scenes, the default camera is set to Metahuman since you cannot control the car. But you may click the button on the screen to change the camera to car's view.

<br>
<br>
<br>



## Experimental Mode

1. Set `DEBUG` to true inside `Settings.config` to view experimental mode.
2. In the `Train` scene, the `RoadEditor` is visible when viewing from the top, after changing the view by `Ctrl + K`.




<br>
<br>
<br>


## Using PyBack

1. Only 2 scenes in this application can be used directly to test `PyBack`.
2. Note that if you want to capture full screen when generating data using `PyBack/generate_data.py`, try to run the application in `Full Screen Mode`.
3. Note that the default IP is localhost while port is 25001, which can be set inside the `settings.config` file.
4. For generating data, use the `Data Sending Mode`.
5. For autonomous driving testing mode, use the `AI Auto Mode`.




<br>
<br>
<br>


---
---

_Developed by Alexander Ezharjan_

**Note**: _Some commercial codes and assets are removed intentionally for copyright concerns._