import metpy
from metpy.calc import relative_humidity_from_dewpoint, heat_index
from metpy.units import units


#heat_index(30 * units.degC, 90 * units.percent)

T = float(input("What is the temperature?\n\n"))*units.degF
d = float(input("What is the Dew Point?\n\n"))*units.degF

#d2rh = round((relative_humidity_from_dewpoint(T,d).to(units.percent)),0)
d2rh = (relative_humidity_from_dewpoint(T,d)).to(units.percent)

print(d2rh)

heat = (heat_index(T,d2rh))

print(type(heat),heat)


print("\n\n"+"The Heat Index is:",str(heat)+chr(176)+'F')

if heat > 99:
    print("This does meet Heat Advisory Criteria")
else:
    print("This is below Heat Advisory Criteria")