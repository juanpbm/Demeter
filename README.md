# Demeter The Bell Pepper Harvester
### Team Members: Amrit Ramesh, Juan Pablo Bernal, Kevin Lewis, Ziyi Yang, Santiago Delgado and Juan Carlos del Pino
 
### Advisor: Professor Taskin Padir

Team Demeter has designed a computer vision system surrounding the Kinova Jaco arm to autonomously pick ripe red bell peppers. 
The basis of this project was an understanding of the deficiencies of current farming practices when it comes to bell peppers. 
More specifically, mechanical harvesters, while very fast, are not very effective at distinguishing between ripe and unripe peppers.
Furthermore, red peppers do not ripen all at once so a harvester must be able to tell between ripe and unripe peppers.
At the same time, more modern robotic harvesters, while very effective at distinguishing ripeness and therefore generally more precise in picking peppers, 
have some limitations when it comes to their high cost and their speed. With that said there currently are not any commercially viable robotic bell pepper pickers.
Ultimately, while we don’t aim to improve on the SOA systems algorithms, hardware, communication, and general speed we do think we can create a rivaled system that
is lighter weight, cheaper, and potentially commercially viable.

For the actual design of the pepper picker, we decided to use a net and blade apparatus attached to the Kinova robotic arm such that we could grab,
cut the stem, and transport the pepper to a basket. In order to actually recognize the pepper, we used a stereo vision camera module that would not
only help us detect ripeness but also help us determine the distance so we can actually pick the pepper. More specifically, as the arm moves,
we used one of the cameras to scan through the field of peppers. Whenever the camera detects red we then stop the movement and used computer vision 
algorithms to move the arm to get that red object fully within the frame. Finally, we create a bounding box around that red object and send that bounding
box image to an ML model that predicts the probability that it is a ripe red bell pepper. In this case, we use the pre-trained ImageNet model trained on the
VGG16 architecture. If the red object is a pepper we will then use the depth of the stereo vision to find the correct 3D position of the target with respect to the arm.
The recognition system was run in a Raspberry Pi 4 Model B that communicated using ROS services to a computer running the arm driver. Moreover, 
a third computer was used to run the machine learning model since the Raspberry Pi was not powerful enough.

To test and validate the system we hung three peppers so that two red would appear in the same frame and a third green pepper would exist to show how the 
system would handle seeing an unripe pepper. This proved the recognition system can handle seeing two peppers and picking one first, and then the other. 
This also proved that the stereo vision gives accurate depth and the hardware can handle cutting through a pepper stem. Results showed that 
Demeter was able to do everything successfully except cut the stem because the fingers of the Jaco arm did not have enough strength. 


## How To Run
This code was run on three computers, a raspberry Pi 4 model B ran the recognition.py in ROS noetic, a computer ran ROS noetic for the MLmodel.py, and a computer connected to the arm ran arm_and_chasis_driver.py using ROS melodic. The two noetic computer were used becuase we couldnt get the pi to use tensorflow need for the ML script, and the computer was running linux subsytem that couldnt use the ports to connect to the camera. Use catkin_make inside each workspace to build required the packages.
