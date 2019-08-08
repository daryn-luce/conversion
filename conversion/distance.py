class Nanometer():

    @staticmethod
    def micrometer(dist):
        return dist / 1000
        
    @staticmethod
    def millimeter(dist):
        return dist / 1e6

    @staticmethod
    def centimeter(dist):
        return dist / 1e7

    @staticmethod
    def meter(dist):
        return dist / 1e9

    @staticmethod
    def kilometer(dist):
        return dist / 1e12

    @staticmethod
    def inch(dist):
        return dist / 2.54e7

    @staticmethod
    def foot(dist):
        return dist / 3.048e8

    @staticmethod
    def yard(dist):
        return dist / 9.144e8

    @staticmethod
    def mile(dist):
        return dist / 1.609e12

    @staticmethod
    def nautical(dist):
        return dist / 1.852e12

class Micrometer():

    @staticmethod
    def nanometer(dist):
        return dist * 1000
        
    @staticmethod
    def millimeter(dist):
        return dist / 1000

    @staticmethod
    def centimeter(dist):
        return dist / 10000

    @staticmethod
    def meter(dist):
        return dist / 1e6

    @staticmethod
    def kilometer(dist):
        return dist / 1e9

    @staticmethod
    def inch(dist):
        return dist / 25400

    @staticmethod
    def foot(dist):
        return dist / 304800

    @staticmethod
    def yard(dist):
        return dist / 914400

    @staticmethod
    def mile(dist):
        return dist / 1.609e+9

    @staticmethod
    def nautical(dist):
        return dist / 1.852e+9

class Millimeter():

    @staticmethod
    def nanometer(dist):
        return dist * 1e6
        
    @staticmethod
    def micrometer(dist):
        return dist * 1000

    @staticmethod
    def centimeter(dist):
        return dist / 10

    @staticmethod
    def meter(dist):
        return dist / 1000

    @staticmethod
    def kilometer(dist):
        return dist / 1e6

    @staticmethod
    def inch(dist):
        return dist / 25.4

    @staticmethod
    def foot(dist):
        return dist / 304.8

    @staticmethod
    def yard(dist):
        return dist / 914.4

    @staticmethod
    def mile(dist):
        return dist / 1.609e+6

    @staticmethod
    def nautical(dist):
        return dist / 1.852e+6
        
class Centimeter():
    @staticmethod
    def nanometer(dist):
        return dist * 1e7
    
    @staticmethod
    def micrometer(dist):
        return dist * 10000

    @staticmethod
    def millimeter(dist):
        return dist * 10
        
    @staticmethod
    def meter(dist):
        return dist / 100
        
    @staticmethod
    def kilometer(dist):
        return dist / 100000

    @staticmethod
    def inch(dist):
        return dist / 2.54
    
    @staticmethod
    def foot(dist):
        return dist / 30.48
    
    @staticmethod
    def yard(dist):
        return dist / 91.44
        
    @staticmethod
    def mile(dist):
        return dist / 160934.4
        
    @staticmethod
    def nautical(dist):
        return dist / 185200

class Meter():
    @staticmethod
    def nanometer(dist):
        return dist * 1e9
    
    @staticmethod
    def micrometer(dist):
        return dist * 1e6

    @staticmethod
    def millimeter(dist):
        return dist * 1000
        
    @staticmethod
    def centimeter(dist):
        return dist * 100
        
    @staticmethod
    def kilometer(dist):
        return dist / 1000

    @staticmethod
    def inch(dist):
        return dist * 39.37
    
    @staticmethod
    def foot(dist):
        return dist * 3.281
    
    @staticmethod
    def yard(dist):
        return dist / 1.094
        
    @staticmethod
    def mile(dist):
        return dist / 1609.344
        
    @staticmethod
    def nautical(dist):
        return dist / 1852