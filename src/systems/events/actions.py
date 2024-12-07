from typing import List
from src.ecs import Component, Entity, System

class Interaction:
    def __init__(self, entity: Entity):
        self.entity = entity  # Reference to the entity this interaction belongs to

    def check_viable_actions(self, other_entity: Entity) -> List[str]:
        viable_actions = []

        # Add more checks for other actions as needed
        if self.entity.get_component(Interactor) and other_entity.get_component(Interactable):
            viable_actions.append("interact")


        return viable_actions
    
    def trigger_action(self, action: str, other_entity: Entity) -> None:
        if action == "interact":
            self.perform_interaction(other_entity)
        else:
            print(f"Action '{action}' is not recognized.")

    def perform_interaction(self, other_entity: Entity):
        print(f"{self.entity.id} interacts with {other_entity.id}.")
