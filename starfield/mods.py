from typing import DefaultDict

class Mods:
    r = DefaultDict(int)

    def display(self):
        for key in sorted(self.r.keys()):
            print(f"{key}: {self.r[key]}")

# Weapon Mods

## Barrels

    # Standard Issue
    def add_standard_barrel(self):
        ''' Add a standard barrel to the weapon '''
        self.r['iron'] += 1
        self.r['sealant'] += 1

    def add_long_barrel(self):
        self.r['iron'] += 1
        self.r['sealant'] += 1
        self.r['nickel'] += 1

    def add_short_barrel(self):
        self.r['iron'] += 1
        self.r['nickel'] += 1


## Optics
    
    # Standard Issue
    def add_iron_sights(self):
        self.r['nickel'] += 1
        self.r['aluminum'] += 1

    def add_medium_scope(self):
        self.r['vanadium'] += 3
        self.r['adhesive'] += 2
        self.r['zero_wire'] += 1
        self.r['chlorosilanes'] += 3

    def add_reflex_sight(self):
        self.r['adhesive'] += 1
        self.r['aluminum'] += 1
        self.r['chlorosilanes'] += 1

    def add_short_scope(self):
        self.r['titanium'] += 2
        self.r['adhesive'] += 1
        self.r['chlorosilanes'] += 2

## Muzzle

    # Standard Issue
    def add_standard_muzzle(self):
        self.r['iron'] += 1
        self.r['nickel'] += 1

    def add_compensator(self):
        self.r['nickel'] += 1
        self.r['aluminum'] += 1

    def add_muzzle_brake(self):
        self.r['titanium'] += 2
        self.r['tungsten'] += 3
        self.r['sealant'] += 2

    def add_suppressor(self):
        self.r['tantalum'] += 3
        self.r['tungsten'] += 2
        self.r['polymer'] += 2

## Grips

    # Standard Issue
    def add_standard_grip(self):
        self.r['aluminum'] += 1
        self.r['sealant'] += 1

    def add_ergonomic_grip(self):
        self.r['adhesive'] += 1
        self.r['aluminum'] += 2

    def add_tactical_grip(self):
        self.r['titanium'] += 1
        self.r['sealant'] += 1

## Laser
    
    # Standard Issue
    def add_standard_foregrip(self):
        self.r['aluminum'] += 1
        self.r['sealant'] += 1

    def add_laser_sight(self):
        self.r['neon'] += 1
        self.r['aluminum'] += 1
        self.r['helium_3'] += 1

    def add_recon_laser_sight(self):
        self.r['vanadium'] += 3
        self.r['adhesive'] += 2
        self.r['zero_wire'] += 2
        self.r['palladium'] += 2

## Magazine and Battery components
    
    # Standard Issue
    def add_standard_magazine(self):
        self.r['tungsten'] += 1
        self.r['lead'] += 1

    def add_armor_piercing_rounds(self):
        self.r['tungsten'] += 2
        self.r['adhesive'] += 1
        self.r['lead'] += 1

    def add_tactical_magazine(self):
        self.r['sealant'] += 1
        self.r['lead'] += 1

## Internal
    
    # Standard
    def add_no_internal_mod(self):
        self.r['aluminum'] += 1
        self.r['sealant'] += 1

    def add_high_velocity(self):
        self.r['titanium'] += 2
        self.r['monopropellant'] += 1
        self.r['adhesive'] += 3
        self.r['platinum'] += 3

    def add_high_powered(self):
        self.r['tantalum'] += 3
        self.r['isocentered_magnet'] += 1
        self.r['adhesive'] += 3
        self.r['titanium'] += 4

    def add_hair_trigger(self):
        self.r['adhesive'] += 3
        self.r['platinum'] += 3
        self.r['zero_wire'] += 1
        self.r['iridium'] += 2

## Receiver

    def add_semi_automatic(self):
        self.r['nickel'] += 2
        self.r['titanium'] += 3
        self.r['sealant'] += 2
        self.r['copper'] += 2

    def add_fully_automatic(self):
        self.r['titanium'] += 4
        self.r['microsecond_regulator'] += 1
        self.r['sealant'] += 3
        self.r['lubricant'] += 4

    def add_burst_fire(self):
        self.r['titanium'] += 4
        self.r['lubricant'] += 3
        self.r['ytterbium'] += 2

mods = Mods()
mods.display()
