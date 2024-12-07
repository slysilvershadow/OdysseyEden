# actions.py
from typing import Dict, Optional
from .skills import Skill

class Action:
    def __init__(self, name: str, skill_impacts: Optional[Dict[str, int]] = None):
        """
        Initialize an action object.

        Parameters:
        - name (str): The name of the action.
        - skill_impacts (dict): A dictionary mapping skill names to experience points.
        """
        self.name: str = name
        self.skill_impacts: Dict[str, int] = skill_impacts or {}

    def apply(self, character_skills: Dict[str, 'Skill']) -> None:
        """
        Apply the action's impact to the character's skills.

        Parameters:
        - character_skills (dict): A dictionary of the character's skills, where keys are skill names, and values are Skill objects.
        """
        for skill_name, exp in self.skill_impacts.items():
            if skill_name in character_skills:
                character_skills[skill_name].add_exp(exp)
                print(f"{self.name} added {exp} experience to {skill_name}.")
            else:
                # Unlock new skill
                new_skill = Skill(name=skill_name, group='default')
                character_skills[skill_name] = new_skill
                new_skill.add_exp(exp) # Add exp to the newly gained skill
                print(f"{self.name} unlocked {skill_name} and added {exp} experience points to it.")
