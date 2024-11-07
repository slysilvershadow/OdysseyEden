from ..utils import constants as con 

biome = con.BIOMES
print(str(biome))

class World:
    def __init__(self):
        self.entities = {}
        self.systems = []
        self.next_entity_id = 0
    
    def create_entity(self):
        entity = Entity(self.next_entity_id)
        self.entities[self.next_entity_id] = entity
        self.next_entity_id += 1
        return entity
		