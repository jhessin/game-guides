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
research.r['titanium'] -= 15
research.r['lubricant'] -= 3

# Breakdown manufactured goods

# Tier 1
# microsecond_regulator
# = 4 europium
# + 2 lithium
# + 1 supercooled_magnet
# + 1 tau_grade_rheostat

for x in range(research.r['microsecond_regulator']):
    research.r['europium'] += 4
    research.r['lithium'] += 2
    research.r['supercooled_magnet'] += 1
    research.r['tau_grade_rheostat'] += 1
    research.r['microsecond_regulator'] -= 1

# Tier 2
# supercooled_magnet
    # = 1 isocentered_magnet
    # + 1 isotopic_coolant

for x in range(research.r['supercooled_magnet']):
    research.r['isocentered_magnet'] += 1
    research.r['isotopic_coolant'] += 1
    research.r['supercooled_magnet'] -= 1

# tau_grade_rheostat
    # = 1 beryllium
    # = 1 copper

for x in range(research.r['tau_grade_rheostat']):
    research.r['beryllium'] += 1
    research.r['copper'] += 1
    research.r['tau_grade_rheostat'] -= 1


# Tier 3

# isocentered_magnet
    # = 1 cobalt
    # + 1 nickel

for x in range(research.r['isocentered_magnet']):
    research.r['cobalt'] += 1
    research.r['nickel'] += 1
    research.r['isocentered_magnet'] -= 1

# isotopic_coolant
    # = 1 ionic_liquids
    # + 1 tetrafluorides

for x in range(research.r['isotopic_coolant']):
    research.r['ionic_liquids'] += 1
    research.r['tetrafluorides'] += 1
    research.r['isotopic_coolant'] -= 1

research.clean()
research.display()
