from mods import Mods
from outposts import Outpost
from researches import Researches

research = Researches()
outpost = Outpost()
mods = Mods()
outpost.add_extractor_aluminum()
outpost.add_power_solar()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
# outpost.add_extractor_aluminum()
# outpost.add_power_solar()
outpost.add_storage_solid()
research.receiver_mod_1()
mods.add_semi_automatic()
(outpost + research + mods).display()
