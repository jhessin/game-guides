from resource_manager import ResourceManager

class Outpost(ResourceManager):
# EXTRACTORS

    # Extractor - Uranium
    def add_extractor_uranium(self):
        self.r['iron'] += 5
        self.r['tungsten'] += 2
        self.r['aluminum'] += 4

    # Extractor - Water Vapor
    def add_extractor_water_vapor(self):
        self.r['benzene'] += 3
        self.r['membrane'] += 4
        self.r['aluminum'] += 5

    # Extractor - Aluminum
    def add_extractor_aluminum(self):
        self.r['iron'] += 5
        self.r['tungsten'] += 2
        self.r['aluminum'] += 4

## POWER ##

    # Wind Turbine
    def add_power_wind(self):
        self.r['nickel'] += 3
        self.r['cobalt'] += 2
        self.r['aluminum'] += 5

    # Solar Array
    def add_power_solar(self):
        self.r['copper'] += 3
        self.r['beryllium'] += 2
        self.r['aluminum'] += 4

    def add_power_generator(self):
        self.r['austenitic_manifold'] += 1
        self.r['tau_grade_rheostat'] += 1
        self.r['isocentered_magnet'] += 1
        self.r['tungsten'] += 4

## STORAGE & TRANSFER ##

    # Transfer Container
    def add_transfer_container(self):
        self.r['lubricant'] += 4
        self.r['iron'] += 8
        self.r['tungsten'] += 5

    # Storage Container - Solid
    def add_storage_solid(self):
        self.r['adaptive_frame'] += 3
        self.r['iron'] += 6
        self.r['aluminum'] += 5

    # Storage - Liquid
    def add_storage_liquid(self):
        self.r['adaptive_frame'] += 3
        self.r['nickel'] += 5
        self.r['aluminum'] += 6

    # Storage - Gas
    def add_storage_gas(self):
        self.r['adaptive_frame'] += 3
        self.r['copper'] += 6
        self.r['tungsten'] += 5

## Misc - Utility ##

    # Scan Booster
    def add_scan_booster(self):
        self.r['copper'] +=3
        self.r['beryllium'] += 2
        self.r['aluminum'] += 4

    # Cargo Link
    def add_cargo_link(self):
        self.r['zero_wire'] += 2
        self.r['iron'] += 20
        self.r['beryllium'] += 2
        self.r['aluminum'] += 12

    # Crew Staiton
    def add_crew_station(self):
        self.r['nickel'] += 3
        self.r['iron'] += 2
        self.r['aluminum'] += 5

    # Landing Pand and Shipbuilder
    def add_landing_pad(self, with_builder = True):
        if with_builder:
            self.r['adaptive_frame'] += 18
            self.r['zero_wire'] += 2
            self.r['iron'] += 30
            self.r['beryllium'] += 2

if __name__ == "__main__":
    outpost = Outpost()
    outpost.add_extractor_aluminum()
    outpost.add_power_solar()
    outpost.add_power_solar()
    outpost.add_power_solar()
    outpost.add_power_solar()
    outpost.add_storage_solid()
    outpost.display()
