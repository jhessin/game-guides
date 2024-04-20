from mods import Mods
from outposts import Outpost
from researches import Researches

research = Researches()
outpost = Outpost()
mods = Mods()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
# outpost.add_storage_solid()
research.receiver_mod_1()
# mods.add_semi_automatic()
# (outpost + research + mods).display()

# Already added to research
research.r['isotopic_coolant'] -= 4
research.r['titanium'] -= 15
research.r['lubricant'] -= 7
research.r['ytterbium'] -= 2

# Checklist - Give it all to Vasco
research.r['beryllium'] -= 1
research.r['cobalt'] -= 2
research.r['copper'] -= 1
research.r['europium'] -= 8
research.r['ionic_liquids'] -= 3
research.r['lithium'] -= 4
research.r['lubricant'] -= 0
research.r['microsecond_regulator'] -= 1
research.r['nickel'] -= 2
research.r['tau_grade_rheostat'] -= 1
research.r['tetrafluorides'] -= 3
research.r['titanium'] -= 0
research.r['ytterbium'] -= 0


# Breakdown manufactured goods

# Tier 1

for x in range(research.r['microsecond_regulator']):
    research.r['europium'] += 4
    research.r['lithium'] += 2
    research.r['supercooled_magnet'] += 1
    research.r['tau_grade_rheostat'] += 1
    research.r['microsecond_regulator'] -= 1

# Tier 2

for x in range(research.r['supercooled_magnet']):
    research.r['isocentered_magnet'] += 1
    research.r['isotopic_coolant'] += 1
    research.r['supercooled_magnet'] -= 1


for x in range(research.r['tau_grade_rheostat']):
    research.r['beryllium'] += 1
    research.r['copper'] += 1
    research.r['tau_grade_rheostat'] -= 1


# Tier 3

for x in range(research.r['isocentered_magnet']):
    research.r['cobalt'] += 1
    research.r['nickel'] += 1
    research.r['isocentered_magnet'] -= 1

for x in range(research.r['isotopic_coolant']):
    research.r['ionic_liquids'] += 1
    research.r['tetrafluorides'] += 1
    research.r['isotopic_coolant'] -= 1

research.clean()
research.display()

print()
print('Target Systems:')
print()
print('==================')
print('System: Altair')
print('Level: 15')
print('==================')
print('Moon: Altair IV-B')
print('Resources: lithium')
print()
print('==================')
print('System: Muphrid')
print('Level: 15')
print('==================')
print('Planet: Muphrid IV')
print('Resources: lubricant')
print('Moon: Muphrid III-A')
print('Resources: ytterbium')
print()
print('==================')
print('System: Bradbury')
print('Level: 20')
print('==================')
print('Planet: Bradbury III')
print('Resources: titanium')
print('Planet: Bradbury I')
print('Resources: ytterbium')
print()
print('==================')
print('System: Hyla')
print('Level: 70')
print('==================')
print('Moon: Hyla VII-A')
print('Resources: lithium & titanium')

