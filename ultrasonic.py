

from time import sleep
from gpiozero import DistanceSensor


sensor = DistanceSensor(echo=23,trigger=24)

try:
	while(True):
		distance = sensor.distance *100
		print(distance)
		
		if distance < 30:
			sleep(2)
			print("Distance :",distance)
		else:
			sleep(2) 
			print("Sensor is deactivated")	
		sleep(0.5)
except KeyboardInterrupt:
	print("Error")



'''
from gpiozero import DistanceSensor
from time import sleep

# Create an instance of DistanceSensor
sensor = DistanceSensor(echo=23, trigger=24)

try:
    while True:
        # Get the distance in meters and convert to cm
        distance = sensor.distance * 100
        print(f"Distance: {distance:.1f} cm")
        sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
'''
