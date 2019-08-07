class Temperature:
    #notable temps
    cel_boil = 100.00
    fah_boil = 212.00 
    kel_boil = 373.15
    
    cel_frz = 0.00
    fah_frz = 32.00
    kel_frz = -273.15
    
    cel_absz = -100
    fah_absz = -459.67
    kel_absz = 0
    
    #Fahrenheit to x
    @staticmethod
    def fah_to_cel(temp):
        return round((temp - 32) * (5/9),2)
        
    @staticmethod
    def fah_to_kel(temp):
        return round((temp - 32) * (5/9) + 273.15,2)
    
    #Celsius to x
    @staticmethod
    def cel_to_fah(temp):
        return round(temp * (9/5) + 32,2)
    
    @staticmethod
    def cel_to_kel(temp):
        return round(temp + 273.15,2)
    
    #Kelvin to x
    @staticmethod    
    def kel_to_fah(temp):
        return round((temp - 273.15) * (9/5) + 32,2)
    
    @staticmethod    
    def kel_to_cel(temp):
        return round(temp - 273.15,2)
        
class Distance:
    
    # Centimeter to x
    @staticmethod
    def cm_to_inch(dist):
        return round(dist / 2.54,2)
    
    @staticmethod
    def cm_to_feet(dist):
        return round(dist / 30.48,2)
    
    @staticmethod
    def cm_to_yard(dist):
        return round(dist / 91.44,2)
        
    @staticmethod
    def cm_to_nm(dist):
        return round(dist * (1e7),2)
    
    @staticmethod
    def cm_to_um(dist):
        return round(dist * 10000,2)

    @staticmethod
    def cm_to_mm(dist):
        return round(dist * 10,2)
        
    @staticmethod
    def cm_to_m(dist):
        return round(dist / 100,2)  
        
    @staticmethod
    def cm_to_km(dist):
        return round(dist / 100000,2)          