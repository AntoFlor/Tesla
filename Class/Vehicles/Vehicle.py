import time

class Vehicle :
    # Constuctor
    def __init__(self, _name):
        self.name = _name
        self.sensors = []
    
    # Accessor and Mutator of "name" attr
    def getName(self):
        return self.name
    
    def setName(self,_name):
        self.name = _name
    
    # Method to add a sensor to the car
    def addSensor(self, Sensor):
        self.sensors.append(Sensor)

    # Method to remove a sensor from the car
    def deleteSensor(self, Sensor):
        self.sensors.remove(Sensor)

    # writes all the information about the car in the console 
    def getVehicleInfo(self):
        print("name : " + self.name)
        """ for sensor in self.sensors :
            sensor.getSensorInfo() """
        for i in range(0,20):
            print(i)
            time.sleep(0.5)

    
