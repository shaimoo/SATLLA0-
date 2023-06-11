import subprocess
command = ['vcgencmd','measure_temp']
try:
	subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
	print (f"An error occurred: {e}")	
