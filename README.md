# SATLLA0-
![image](https://github.com/shaimoo/SATLLA0-/assets/92544909/62848a76-3103-445a-bc18-e6417797a001)

## Overview
SATLLA-0 (also known as satllazero) is an open source project dedicated to the development of a complete pico-satellite.<br>

## Our Vision
The overall vision is to enable both researchers and 12K to build a fully functional pico-satellite model based on a proven design that is fully functional in space (see SATLLA-2B). The SATLLA-0 project includes both the software and hardware of the pico satellite (and ground station). The vision of the project is to enable any science class (in high school or university) to experience the "new space" at a fraction of the price of existing solutions.<br><br>

Introduction: <br>
The field of space engineering is an exciting and rapidly growing area of study that deals with the design, construction, and operation of spacecraft and their associated systems. The development of satellites is a critical aspect of space engineering as they play a vital role in communication, earth observation, navigation, and scientific research. <br>
The SATLLA-0 project is an open-source initiative dedicated to the development of a fully functional pico-satellite. The project aims to provide an affordable solution for researchers and students to build a laboratory or functional nanosatellite based on a proven design that is fully functional in space. The project includes both the software and hardware of the pico-satellite and ground station, making it an all-in-one solution.<br>
The SATLLA-0 core flight system is an open-source flight software used by the SATLLA-2B satellite. It is designed to be a starting point for academic institutions or schools that want to build or experiment with a laboratory or functional nanosatellite. The software is written in Arduino, which is a C/C++ based programming language that is open source and easy to learn.<br>
The SATLLA-0 flight software platform includes a functional nanosatellite based on a Teansy microcontroller that supports various subsystems such as the electrical power system (EPS), telecommand and communications based on LoRa UHF and S-band, GPS, inertial measurement unit (IMU), thermistors (Temperature), high-power array LED, and an on-board computer (OBC) for research activities based on a RaspberryPi Zero. The software also<br>

In our version we built a satellite in a two-dimensional way so that everything is laid out on the table. <br>
With the help of raspberry pi cube cell, a power bank, a camera, cables and a memory card. <br>

## Install
SATLLA-0 is written in Arduino, and can be installed via Arduino, Teensyduino or any other IDE supporting Arduino.<br>
OBC - Raspberry Pi Z2 <br>
Install RPi OS Lite (32bit) on an SD card How to install and set up raspberry pi OS into SD card  || Pi4 desktop Step <br>
Set hostname<br>
Enable SSH<br>
If your using a RPi native camera:<br>
Sudo raspi-config<br>
Interface Options<br>
Legacy Camera<br>
Yes<br>
Reboot<br><br><br>


Instructions<br>

First download the Raspberry Pi software  https://www.raspberrypi.com/softwar <br>
Click this button    <br>

First connect the memory card to the computer using an adapter, then first burn the operating system on the memory card and insert it into the Raspberry Pi, after the operating system comes up, you need to choose a username and password, then enter cmd, activate upgrade, make updates to the most recent versions, you can watch this video
 https://www.youtube.com/watch?v=2AhCWJ6YQHk&t=13s
Download python3 https://www.python.org/downloads/<br>

We connected a camera to a Raspberry Pi, we wrote a script in the terminal to check that it works, that the camera works and takes a picture and saves it:  raspistill -o Desktop/image.jpg.
We need to check that the Raspberry Pi we are using is sufficient to connect the camera or we need to give it all the settings otherwise it will not work.<br>

We created communication between our Raspberry Pi and another computer in order to communicate using the SSH communication protocol.<br>

We used SSH to work remotely.<br>

We issued a match between the Raspberry Pi and the controller (arduino compatible cube cell AB02) by serial using rx tx pins. so that the controller sends a command and according to this the Raspberry Pi runs a script written on it in a certain folder and is numbered randomly for each command received a number.<br>

The first command will take a picture and it will be saved in the pictures folder.<br>

A second command will group the size of the selected image and it will be saved in the images folder.<br>

A third command that sends the temperature of the raspberry pi.<br>

We improved boot so that it would be faster, so we changed the processor usage power, entered the boot folder and entered the config.txt folder, where we changed the arm_freq=1300 , over_voltage=2, the default.<br>


 We wrote the controller commands in arduino for download
https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE <br>



We made a connection between our ground station which is also (arduino compatible cube cell AB02) and our controller using Lora so that the commands we request from the satellite will come from the ground station so that the ground station listens to the satellite and sends requests and also the opposite direction the satellite sends messages and listens to requests.<br>

<br><br><br>



Follow this OBC setup:<br>
## OBC Setup
enable serial0<br>
sudo nano /boot/cmdline.txt<br>
remove the line: "console=serial0,115200"<br>
sudo reboot<br>
Update config.txt file with the contents of the config file in this directory<br>
sudo nano /boot/config.txt<br>
rewrite contents<br>
Expand file system<br>
sudo raspi-config<br>
Advanced options -> Expand Filesystem<br>
Increase swap<br>
sudo dphys-swapfile swapoff<br>
sudo nano /etc/dphys-swapfile<br>
modify the variable to be CONF_SWAPSIZE=1024<br>
sudo dphys-swapfile setup<br>
sudo dphys-swapfile swapon<br>
Prepare git<br>
sudo apt update<br>
sudo apt-get update<br>
sudo apt upgrade<br>
sudo apt install git<br>
Prepare python and pip<br>
sudo apt install python3-pip<br>
python3 -m pip install --upgrade pip<br>
sudo apt-get install libatlas-base-dev<br>
sudo apt install python3-picamera<br>
Required for 'convert'<br>
sudo apt-get install imagemagick<br>
Required for 'pillow'<br>
sudo apt install libjpeg-dev<br>
Required for 'opencv'<br>
sudo apt install cmake build-essential pkg-config git<br>
sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev<br>
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev<br>
sudo apt install libgtk-3-dev libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5<br>
sudo apt install libatlas-base-dev liblapacke-dev gfortran<br>
sudo apt install libhdf5-dev libhdf5-103<br>
sudo apt install python3-dev python3-pip python3-numpy<br>
python3 -m pip install opencv-python==4.5.3.56<br><br>


Install the requirements file<br>
sudo pip install -r satllazero/SAT0_OBC/setup/requirements.txt<br>
More installs<br>
sudo apt-get install pigpio<br>
sudo pip3 install pigpio<br>
sudo apt-get install ninja<br>
crontab<br>
sudo crontab -e<br>
@reboot /usr/bin/pigpiod<br>
create sat service<br>
sudo cp satllazero/SAT0_OBC/setup/sat.service /lib/systemd/system/.<br>
load sat service<br>
sudo reboot<br>
sudo systemctl daemon-reload<br>
sudo systemctl enable sat.service<br>
sudo systemctl start sat<br>
sudo systemctl stop sat<br>
sudo systemctl restart sat<br>











![image](https://github.com/shaimoo/SATLLA0-/assets/92544909/bb0d14f9-68fb-4c29-9870-fc5780701c1d)<br>





In the picture you can see the connection of the camera to the Raspberry Pi, the card we burned goes into the Raspberry Pi, we connected the USB connection to a computer screen in order to work with it. The white cable is a connection to the electricity because it is a satellite so we connected it to the power bank we soldered the legs of the controller and the soldering of the Raspberry Pi where are the RX TX GROUND in order to connect the wires that are connected to the Raspberry Pi to the appropriate legs you can see the picture we collected the number of legs that need to be connected in our case 6,8,10 we connect to the controller and we connect the controller to the computer, through it we give commands to the Raspberry Pi. Among the commands that can be sent to him are reading and writing messages.<br>







 


It is actually our ground station with which we communicate with a satellite through Lora, which both listens to the satellite and sends requests to it, and in the opposite direction. That the communication can be remote like real satellite in the space independent.<br>

## how to run <br>
To run the project, follow these steps:

- Download the project files from the Git repository by clicking on the green button above.
- Connect the Cubecell device to your computer using a USB cable.
- Burn the sender code onto the Cubecell device for the ground station.
- Burn the Cubecell receiver code onto the other Cubecell device.
- Connect all the necessary cables to the Raspberry Pi.
- Clone the Git repository onto the Raspberry Pi.
- Open the terminal on the Raspberry Pi and navigate to the project directory.
- Run the read.py script from the terminal on the Raspberry Pi.
- On the ground station, run the pc_receive_file.py script.
- Connect the Cubecell device to the ground station.
- Now you can use a few commands to interact with the system:
- To check the temperature of the Raspberry Pi, use the command: temperature. This will print the temperature reading.
- To take a picture using the connected camera, use the command: take a picture.
- To compress the captured image and send it via LoRa, use the command: send.
Make sure to follow the instructions carefully and ensure that all the dependencies are installed on the Raspberry Pi and the ground station

