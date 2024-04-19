from enum import Enum

class ResourceType(Enum):
    Organic = 0
    Inorganic = 1
    Manufactured = 2

class Resource:
    name: str
    rt: ResourceType = ResourceType.Organic
    rarity: int = 0
    value: int = 0
    mass: float = 1.0

    def __init__(self,
                 name: str, 
                 rt: ResourceType = ResourceType.Organic, 
                 rarity: int = 0,
                 value: int = 0,
                 mass: float = 1.0
                 ):
        self.name = name
        self.rt = rt
        self.rarity = rarity
        self.value = value
        self.mass = mass

InorganicResources = [
        Resource('Aldumite', ResourceType.Inorganic, 4, 84, 1.9),
        Resource('Alkanes', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Aluminum', ResourceType.Inorganic, 0, 7, 0.5),
        Resource('Antimony', ResourceType.Inorganic, 3, 30, 0.8),
        Resource('Aqueous Hematite', ResourceType.Inorganic, 4, 56, 1.3),
        Resource('Argon', ResourceType.Inorganic, 1, 5, 0.5),
        Resource('Benzene', ResourceType.Inorganic, 1, 19, 0.6),
        Resource('Beryllium', ResourceType.Inorganic, 1, 12, 0.5),
        Resource('Caelumite', ResourceType.Inorganic, 3, 264, 0.3),
        Resource('Caesium', ResourceType.Inorganic, 3, 25, 0.8),
        Resource('Carboxylic Acids', ResourceType.Inorganic, 4, 12, 0.8),

        Resource('Chlorine', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Chlorosilanes', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Cobalt', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Copper', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Dysprosium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Europium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Fluorine', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Gold', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Helium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Indicite', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Ionic Liquids', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Iridium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Iron', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Lead', ResourceType.Inorganic, 1, 13, 0.6),

        Resource('Lithium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Mercury', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Neodymium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Neon', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Nickel', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Palladium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Platinum', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Plutonium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Rothicite', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Silver', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Tantalum', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Tasine', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Tetrafluorides', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Titanium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Tungsten', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Uranium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Vanadium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Veryl', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Vytinium', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Water', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Xenon', ResourceType.Inorganic, 1, 13, 0.6),
        Resource('Ytterbium', ResourceType.Inorganic, 1, 13, 0.6),
        ]

