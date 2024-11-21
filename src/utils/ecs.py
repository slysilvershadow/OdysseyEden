import uuid

class Entity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component
        return self

    def get_component(self, component_type):
        return self.components.get(component_type, None)

    def remove_component(self, component_type):
        if component_type in self.components:
            del self.components[component_type]


class Component:
    def __init__(self):
        self.id = uuid.uuid4()


class System:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        """Add an entity if it matches the filter criteria."""
        if self.filter(entity):
            self.entities.append(entity)

    def remove_entity(self, entity):
        """Remove an entity from the system."""
        if entity in self.entities:
            self.entities.remove(entity)

    def filter(self, entity):
        """Override this method in subclasses to define criteria."""
        return False

    def update(self, dt):
        """Override this method in subclasses to define system logic."""
        raise NotImplementedError("Subclasses should implement this!")


class EntityManager:
    def __init__(self):
        self.entities = {}

    def create_entity(self):
        """Create a new entity and store it."""
        entity = Entity()
        self.entities[entity.id] = entity
        return entity

    def remove_entity(self, entity_id):
        """Remove an entity by its ID."""
        if entity_id in self.entities:
            del self.entities[entity_id]


class SystemManager:
    def __init__(self):
        self.systems = []

    def add_system(self, system):
        """Register a system with the manager."""
        self.systems.append(system)

    def update(self, entities, dt):
        """Update all systems with relevant entities."""
        for system in self.systems:
            for entity in entities:
                if entity not in system.entities:
                    system.add_entity(entity)
                # No need to recheck `filter` if already removed.
            system.update(dt)
