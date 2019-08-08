from conversion.temperature import Fahrenheit as f
from conversion.distance import Nanometer as n
from conversion import temperature as t
from conversion.base2 import Gigabyte as G

print(t.Kelvin.celsius(245),'C')
print(f.celsius(77),'C')
print(n.kilometer(300),'km')

print(G.kilobyte(842))