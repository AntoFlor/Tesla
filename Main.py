# Add modules path to python interpreter
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Class', 'Vehicles'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Class', 'Sensors'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Class', 'Motors'))

# Import Class from modules
from Vehicle  import *
from Sensor import *
from UltrasonicSensor import *

# Imports to use threads
import logging
import threading
import time

# Creating methods


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

# Start the code
if __name__ == "__main__":
    # Create the car
    car = Vehicle("group5's car")

    # Create car's addons
    sensor = Sensor("nigga")
    sensor1 = Sensor("nigga1")

    # Add addons to the car
    car.addSensor(sensor)
    car.addSensor(sensor1)
    car.deleteSensor(sensor)

    for sensor in car.sensors :
        print(sensor.name)

    

    

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=car.getVehicleInfo, args=())
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : wait for the thread to finish")
    #x.join()
    logging.info("Main    : all done")