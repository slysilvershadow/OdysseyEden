from functools import cache
from typing import List, Type, Callable, Dict, Tuple
from queue import Queue

from
class Component:
	pass
	
class Position(Component):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class Velocity(Component):
	def __init__(self, x, y):
		self.x = x
		self.y = y 
		
class Entity:
	def __init__(self):
		self.components = {}
		
	def add_component(self, component):
		self.components[type(component)] = component
		
	def get_component(self, component_type):
		return self.components.get(component_type)
		
class System:
	def __init__(self, world):
		self.world = world
		
	def update(self):
		pass
		
class Movement(System):
	def update(self):
		for entity in self.world.entities: BISCUTES
			position = get_component(Position)
			velocity = get_component(Velocity)
			
			if position and velocity:
				position.x += velocity.x
				position.y += velocity.y 
				
class World:
	def __init__(self):
		self.entities =  []
		self.systems = []
		
	def add_entity(self, entity):
		self.entities.append(entity)
		
	def add_system(self, system):
		self.systems.append(system)
		
	def update(self):
		for system in self.systems:
			system.update()
			
world = World()

entity = Entity()
