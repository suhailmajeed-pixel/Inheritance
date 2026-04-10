class vehical : 
    def __init__(self , name , max_speed , mileage ):
        self.name = name 
        self.max_speed = max_speed 
        self.mileage = mileage 

class bus(vehical):
    pass 
school_bus = bus ("school vo1vo", 180 , 12)
print ("vehical name:",school_bus.name , "speed :",school_bus.max_speed , "milage :",school_bus.mileage)