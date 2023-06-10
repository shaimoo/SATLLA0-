import serial

# Open the serial connection to the CubeCell destination (PC)
ser = serial.Serial('/dev/ttyUSB1', 115200)

# Read the picture data from the CubeCell destination (PC)
picture_data = ser.read()

# Save the received picture data to a file
with open('received_picture.jpg', 'wb') as file:
    file.write(picture_data)

# Close the serial connection
ser.close()
