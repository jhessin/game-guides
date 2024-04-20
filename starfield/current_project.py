from resource_manager import ResourceManager

rm = ResourceManager()

# Weapon Workbench
rm.r['adhesive'] += 3
rm.r['iron'] += 4
rm.r['sealant'] += 3
rm.r['nickel'] += 2

# Already added to research
# rm.r['isotopic_coolant'] -= 4

# Checklist - Give it all to Vasco
rm.r['adhesive'] -= 0
rm.r['iron'] -= 4
rm.r['nickel'] -= 2
rm.r['sealant'] -= 3

# Breakdown manufactured goods

# Tier 1

# for x in range(research.r['microsecond_regulator']):
#     research.r['europium'] += 4
#     research.r['lithium'] += 2
#     research.r['supercooled_magnet'] += 1
#     research.r['tau_grade_rheostat'] += 1
#     research.r['microsecond_regulator'] -= 1

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

