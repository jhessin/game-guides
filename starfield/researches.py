from resource_manager import ResourceManager
from mods import Mods

# Weapon Mods
class Researches(ResourceManager):

    def grip_and_stock_mods_3(self):
        ''' Add grip and stock research '''
        self.r['polymer'] += 10
        self.r['adhesive'] += 20

    def receiver_mod_1(self):
        self.r['isotopic_coolant'] += 5
        self.r['microsecond_regulator'] += 3
        self.r['ytterbium'] += 10
        self.r['titanium'] += 30
        self.r['lubricant'] += 10


if __name__ == "__main__":
    research = Researches()
    mods = Mods()
    research.receiver_mod_1()
    mods.add_laser_sight()
    (research + mods).display()
