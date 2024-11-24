from resource_manager import ResourceManager

rm = ResourceManager()

"""Reasearch Projects Go Here"""


""" SHOPPING LIST HERE """ 
def shopping_list():
    pass
    # EXP Earring
    rm.r['fury_stone'] += 1
    rm.r['power_stone'] += 1
    rm.r['mythril_stone'] += 1
    rm.r['serenity_power'] += 1
    rm.r['dark_matter'] += 3

    # Guard Earring
    rm.r['bright_shard'] += 3
    rm.r['frost_shard'] += 1
    rm.r['mythril_shard'] += 3

    # Rune Armlet
    rm.r['blaze_gem'] += 3
    rm.r['frost_gem'] += 3
    rm.r['thunder_gem'] += 3

    # Moogle Badge
    rm.r['blazing_stone'] += 1
    rm.r['frost_stone'] += 1
    rm.r['lightning_stone'] += 1
    rm.r['mythril'] += 5
    rm.r['orichalcum'] += 3

    # Mega-Eather
    rm.r['blaze_shard'] += 1
    rm.r['frost_shard'] += 1
    rm.r['thunder_shard'] += 1
    rm.r['mythril'] += 5
    pass

"""Here is everything we already have subtracted from the inventory."""
def aquired():
    pass
    # INVENTORY
    rm.r['blaze_gem'] -= 5
    rm.r['blaze_shard'] -= 4
    rm.r['mythril_shard'] -= 11
    rm.r['orichalcum'] -= 6
    rm.r['thunder_gem'] -= 3
    pass


"""Break down manufactured goods here"""
def manufacture():
    pass
    # Tier 1

    for x in range(rm.r['microsecond_regulator']):
        rm.r['europium'] += 4
        rm.r['lithium'] += 2
        rm.r['supercooled_magnet'] += 1
        rm.r['tau_grade_rheostat'] += 1
        rm.r['microsecond_regulator'] -= 1

    for x in range(rm.r['zero_wire']):
        rm.r['copper'] += 1
        rm.r['silver'] += 1
        rm.r['zero_wire'] -= 1

    for x in range(rm.r['monopropellant']):
        rm.r['alkanes'] += 2
        rm.r['mag_pressure_tank'] += 1
        rm.r['reactive_gauge'] += 1
        rm.r['monopropellant'] -= 1


    # Tier 2

    for x in range(rm.r['supercooled_magnet']):
        rm.r['isocentered_magnet'] += 1
        rm.r['isotopic_coolant'] += 1
        rm.r['supercooled_magnet'] -= 1


    for x in range(rm.r['tau_grade_rheostat']):
        rm.r['beryllium'] += 1
        rm.r['copper'] += 1
        rm.r['tau_grade_rheostat'] -= 1

    for x in range(rm.r['reactive_gauge']):
        rm.r['copper'] += 1
        rm.r['aluminum'] += 2
        rm.r['reactive_gauge'] -= 1


    # Tier 3

    for x in range(rm.r['isocentered_magnet']):
        rm.r['cobalt'] += 1
        rm.r['nickel'] += 1
        rm.r['isocentered_magnet'] -= 1

    for x in range(rm.r['isotopic_coolant']):
        rm.r['ionic_liquids'] += 1
        rm.r['tetrafluorides'] += 1
        rm.r['isotopic_coolant'] -= 1

shopping_list()
aquired()
# manufacture()
rm.clean()
rm.display()

print()
print("The Sumati's moon, Andraphon, in the Narion system is a famous choice to establish this XP Farming outpost")

