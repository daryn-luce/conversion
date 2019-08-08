class Fahrenheit():
    def __init__(self):
        self.boil = 212.00
        self.freeze = 32.00
        self.zero = -459.67
        
    @staticmethod
    def celsius(temp):
        return round((temp - 32) * (5/9),2)
        
    @staticmethod
    def kelvin(temp):
        return round((temp - 32) * (5/9) + 273.15,2) 

class Celsius():
    def __init__(self):
        self.boil = 100.00
        self.freeze = 0.00
        self.zero = -273.15

    @staticmethod
    def fahrenheit(temp):
        return round(temp * (9/5) + 32,2)
    
    @staticmethod
    def kelvin(temp):
        return round(temp + 273.15,2)

class Kelvin():
    def __init__(self):
        self.boil = 373.15
        self.freeze = -273.15
        self.zero = 0.00

    @staticmethod    
    def fahrenheit(temp):
        return round((temp - 273.15) * (9/5) + 32,2)
    
    @staticmethod    
    def celsius(temp):
        return round(temp - 273.15,2)