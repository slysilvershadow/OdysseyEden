from typing import List
from src.ecs import Component, Entity, System

class Interaction(System):
    def __init__(self):
        super().__init__()

    def check_viable_actions(self, entity1: Entity, entity2: Entity) -> List[str]:
        viable_actions = []

        # Example checks based on components
        if entity1.get_component(Position) and entity2.get_component(Position):
            viable_actions.append("move closer")

        if entity1.get_component(Interactable) and entity2.get_component(Interactor):
            viable_actions.append("interact")

        if entity1.get_component(Combatant) and entity2.get_component(Combatant):
            viable_actions.append("fight")

        return viable_actions

    def add_entity(self, entity: Entity, required_components: List[type]):
        super().add_entity(entity, required_components)