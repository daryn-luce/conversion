class Bit():
    @staticmethod
    def byte(size):
        return size / 8

    @staticmethod
    def kilobyte(size):
        return size / 8000

    @staticmethod
    def megabyte(size):
        return size / 8e+6

    @staticmethod
    def gigabyte(size):
        return size / 8e+9
    
    @staticmethod
    def terabyte(size):
        return size / 8e+12
        
    @staticmethod
    def petabyte(size):
        return size / 8e+15
        
class Byte():
    @staticmethod
    def bit(size):
        return size * 8

    @staticmethod
    def kilobyte(size):
        return size / 1000

    @staticmethod
    def megabyte(size):
        return size / 1e+6

    @staticmethod
    def gigabyte(size):
        return size / 1e+9
    
    @staticmethod
    def terabyte(size):
        return size / 1e+12
        
    @staticmethod
    def petabyte(size):
        return size / 1e+15
        
class Kilobyte():
    @staticmethod
    def bit(size):
        return size * 8000

    @staticmethod
    def byte(size):
        return size * 1000

    @staticmethod
    def megabyte(size):
        return size / 1000

    @staticmethod
    def gigabyte(size):
        return size / 1e+6
    
    @staticmethod
    def terabyte(size):
        return size / 1e+9
        
    @staticmethod
    def petabyte(size):
        return size / 1e+12

class Megabyte():
    @staticmethod
    def bit(size):
        return size * 8e6

    @staticmethod
    def byte(size):
        return size * 1e6

    @staticmethod
    def kilobyte(size):
        return size * 1000

    @staticmethod
    def gigabyte(size):
        return size / 1000
    
    @staticmethod
    def terabyte(size):
        return size / 1e+6
        
    @staticmethod
    def petabyte(size):
        return size / 1e+9

class Gigabyte():
    @staticmethod
    def bit(size):
        return size * 8e9

    @staticmethod
    def byte(size):
        return size * 1e9

    @staticmethod
    def kilobyte(size):
        return size * 1e6

    @staticmethod
    def megabyte(size):
        return size * 1000
    
    @staticmethod
    def terabyte(size):
        return size / 1000
        
    @staticmethod
    def petabyte(size):
        return size / 1e+6

class Terabyte():
    @staticmethod
    def bit(size):
        return size * 8e12

    @staticmethod
    def byte(size):
        return size * 1e12

    @staticmethod
    def kilobyte(size):
        return size * 1e9

    @staticmethod
    def megabyte(size):
        return size * 1e6
    
    @staticmethod
    def gigabyte(size):
        return size * 1000
        
    @staticmethod
    def petabyte(size):
        return size / 1000

class petabyte():
    @staticmethod
    def bit(size):
        return size * 8e15

    @staticmethod
    def byte(size):
        return size * 1e15

    @staticmethod
    def kilobyte(size):
        return size * 1e12

    @staticmethod
    def megabyte(size):
        return size * 1e9
    
    @staticmethod
    def gigabyte(size):
        return size * 1e6
        
    @staticmethod
    def petabyte(size):
        return size * 1000        