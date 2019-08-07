class Temperature:

    @staticmethod
    def fah_to_cel(temp):
        return round((temp - 32) * 5/9,2)
        
    @staticmethod
    def fah_to_kel(temp):
        return round((temp - 32) * 5/9 + 273.15,2)
        
    @staticmethod
    def cel_to_fah(temp):
        pass
    
    @staticmethod
    def cel_to_kel(temp):
        pass
    
    @staticmethod    
    def kel_to_fah(temp):
        pass
    
    @staticmethod    
    def kel_to_cel(temp):
        pass
        
    cel_boil = 100.00
    fah_boil = 212.00 
    kel_boil = 373.15
    