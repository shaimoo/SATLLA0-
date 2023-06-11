import subprocess
import time


i=0
while i<1:
	command = ['raspistill', '-o' ,'/home/satlla0/Desktop/scripts/'+str(i)+'.jpg']
	try:
		subprocess.run(command, check=True)
		print("image capture successfully.")
	except subprocess.CalledProcessError as e:
		print (f"An error occurred: {e}")	
	i+=1


