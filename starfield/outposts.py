## EXTRACTORS ##

# Extractor - Uranium
iron = 5
tungsten = 2
aluminum = 4

# Extractor - Water Vapor
benzene = 3
membrane = 4
aluminum += 5

# Extractor - Aluminum
iron += 5
tungsten += 2
aluminum += 4

## POWER ##

# Wind Turbine
nickel = 3
cobalt = 2
aluminum += 5

# Solar Array
copper = 3
beryllium = 2
aluminum += 4

## STORAGE & TRANSFER ##

# Transfer Container
lubricant = 4
iron += 8
tungsten += 5

# Storage Container - Solid
adaptive_frame = 3
iron += 6
aluminum += 5

# Storage - Liquid
adaptive_frame += 3
nickel += 5
aluminum += 6

# Storage - Gas
adaptive_frame += 3
copper += 6
tungsten += 5

## Misc - Utility ##

# Scan Booster
copper +=3
beryllium += 2
aluminum += 4

# Cargo Link
zero_wire = 2
iron += 20
beryllium += 2
aluminum += 12

# Crew Staiton
nickel += 3
iron += 2
aluminum += 5

# Landing Pand and Shipbuilder
adaptive_frame += 18
zero_wire += 2
iron += 30
beryllium += 2

print("adaptive_frame: ", adaptive_frame)
print("aluminum: ", aluminum)
print("benzene: ", benzene)
print("beryllium: ", beryllium)
print("cobalt: ", cobalt)
print("copper: ", copper)
print("iron: ", iron)
print("lubricant: ", lubricant)
print("membrane: ", membrane)
print("nickel: ", nickel)
print("tungsten: ", tungsten)
print("zero_wire: ", zero_wire)
