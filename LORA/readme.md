recive this is the cubecell of the restberypi. <br>
sender this is the pc ground station cubecell.

# CubeCell AB02 Guide
This guide will provide you with step-by-step instructions on how to use the CubeCell AB02, a LoRaWAN development board, to help you get started with your projects. Please follow the instructions below:

## Table of Contents
Introduction
Hardware Setup
Software Setup
Getting Started with Arduino IDE
LoRaWAN Configuration
Sample Code
Additional Resources

## Introduction
The CubeCell AB02 is a compact LoRaWAN development board based on the ASR6501 MCU, which integrates an RF transceiver for long-range communication. It is designed to be easy to use and supports various sensors and peripherals, making it suitable for a wide range of IoT applications.

## Hardware Setup
Connect the CubeCell AB02 to your computer using a micro USB cable.<br>
Ensure that the board is powered on.


## Software Setup
Install the Arduino IDE from the official Arduino website (https://www.arduino.cc/en/software) if you haven't already done so.<br>
Launch the Arduino IDE.<br>
Go to File -> Preferences and in the Additional Boards Manager URLs field, enter the following URL: https://github.com/heltec-automation/cubecell-arduino/raw/master/package_CubeCell_index.json<br>
Click OK to save the preferences.<br>
Go to Tools -> Board -> Boards Manager.<br>
In the Boards Manager window, search for "CubeCell" and click on the CubeCell entry that appears.<br>
Click on Install to install the CubeCell boards package.<br>
Once the installation is complete, close the Boards Manager window.<br>

## Getting Started with Arduino IDE
Connect the CubeCell AB02 to your computer if it's not already connected.<br>
Launch the Arduino IDE.<br>
Go to Tools -> Board and select CubeCell-Board.<br>
Go to Tools -> Port and select the appropriate COM port for the CubeCell AB02.<br>
Open the Blink example sketch by going to File -> Examples -> 01.Basics -> Blink.<br>
Verify that the Board and Port settings are correct.<br>
Click on the Upload button to compile and upload the sketch to the CubeCell AB02.<br>
Once the upload is complete, the LED on the board should start blinking.<br>

## LoRaWAN Configuration
Open the OTAA example sketch by going to File -> Examples -> LoRa -> LoRaWAN_OTAA.
Configure the LoRaWAN parameters in the sketch, including APP_EUI, APP_KEY, DEV_EUI, and LORAWAN_REGION. Refer to your LoRaWAN network provider's documentation for these values.
Verify that the Board and Port settings are still correct.
Click on the Upload button to compile and upload the sketch to the CubeCell AB02.
Once the upload is complete, open the Serial Monitor by going to Tools -> Serial Monitor.
Set the baud rate to 115200 and ensure that the line ending is set to Newline.
You should see the device joining the LoRaWAN network and displaying the relevant information in the Serial Monitor.

## Sample Code
The CubeCell AB02 comes with a variety of example sketches that demonstrate different functionalities. To access the examples, go to File -> Examples -> LoRa or CubeCell and explore the available sketches. These examples cover topics such as sensor readings, GPS, LoRaWAN communication, and more.

## Additional Resources
For more information and resources, refer to the following:

CubeCell GitHub Repository
CubeCell Wiki
Heltec Community Forum
Feel free to explore the provided resources, experiment with different sketches, and adapt the code to suit your specific project requirements.

Happy coding with CubeCell AB02!
