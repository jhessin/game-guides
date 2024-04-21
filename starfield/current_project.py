from resource_manager import ResourceManager

rm = ResourceManager()

# Semi-automatic receiver
# rm.r['copper'] += 3
# rm.r['titanium'] += 4
# rm.r['nickel'] += 3
# rm.r['sealant'] += 2

# Optic and Laser Mods 3 - DONE

# Greenhouse
rm.r['sealant'] += 3
rm.r['reactive_gauge'] += 3
rm.r['adaptive_frame'] += 3
rm.r['fluorine'] += 4

rm.r['aluminum'] += 5
rm.r['nickel'] += 3
rm.r['cobalt'] += 2

# Recon Laser Sight
rm.r['adhesive'] += 3
rm.r['paladium'] += 2
rm.r['vanadium'] += 3
rm.r['zero_wire'] += 4


# Already added to resear333ch
# rm.r['isotopic_coolant'] -= 4

# Checklist - Give it all to Vasco
# rm.r['adaptive_frame'] -= 16
# rm.r['adhesive'] -= 0
# rm.r['copper'] -= 16
# rm.r['fluorine'] -= 0
# rm.r['paladium'] -= 13
# rm.r['reactive_gauge'] -= 12
# rm.r['sealant'] -= 99
# rm.r['silver'] -= 0
# rm.r['vanadium'] -= 6
# rm.r['zero_wire'] -= 0


# Breakdown manufactured goods

# Tier 1

# for x in range(research.r['microsecond_regulator']):
#     research.r['europium'] += 4
#     research.r['lithium'] += 2
#     research.r['supercooled_magnet'] += 1
#     research.r['tau_grade_rheostat'] += 1
#     research.r['microsecond_regulator'] -= 1
# 
for x in range(rm.r['zero_wire']):
    rm.r['copper'] += 1
    rm.r['silver'] += 1
    rm.r['zero_wire'] -= 1

# Tier 2

# for x in range(research.r['supercooled_magnet']):
#     research.r['isocentered_magnet'] += 1
#     research.r['isotopic_coolant'] += 1
#     research.r['supercooled_magnet'] -= 1
#
#
# for x in range(research.r['tau_grade_rheostat']):
#     research.r['beryllium'] += 1
#     research.r['copper'] += 1
#     research.r['tau_grade_rheostat'] -= 1


# Tier 3

# for x in range(research.r['isocentered_magnet']):
#     research.r['cobalt'] += 1
#     research.r['nickel'] += 1
#     research.r['isocentered_magnet'] -= 1
#
# for x in range(research.r['isotopic_coolant']):
#     research.r['ionic_liquids'] += 1
#     research.r['tetrafluorides'] += 1
#     research.r['isotopic_coolant'] -= 1

rm.clean()
rm.display()

print()
print('Arcturus II has a TON of organic resources!')

