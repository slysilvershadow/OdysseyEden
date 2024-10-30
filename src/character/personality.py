# personality.py

import random
from typing import Optional, Dict
from ..utils.constants import AGES, PERSONALITY_CATAGORIES, TRAITS, TRAIT_SYNERGIES, TRAIT_EVOLUTIONS


class Trait:
    def __init__(self, name: str, age_group: str, trait_group: str, synergy: Dict, passive_effect: Optional[str] = None):
        """
        Initialize a Trait object.

        Parameters:
        - name (str): The name of the trait.
        - age_group (str): The age group when this trait was acquired (e.g., 'Child', 'Teen').
        - trait_group (str): The category this trait belongs to (e.g., 'Personality', 'Skill').
        - synergy (dict): A dictionary mapping traits that synergize with this one.
        - passive_effect (str): A passive effect the trait provides, if any.
        """
        self.name: str = name
        self.age_group: str = age_group
        self.trait_group: str = trait_group
        self.synergy: Dict = synergy
        self.passive_effect: Optional[str] = passive_effect

    def evolve(self, current_age_group: str) -> None:
        """
        Evolve the current trait based on the character's current age group.

        Parameters:
        - current_age_group (str): The age group the character is currently in.

        This function checks the predefined evolutions (in TRAIT_EVOLUTIONS) for the trait and updates it if applicable.
        """
        self.current_age_group = current_age_group
        for evolution in TRAIT_EVOLUTIONS:
            if self.name == evolution[0] and self.age_group == evolution[1]:
                self.name = evolution[2]  # Evolve to the next trait
                print(f"Evolved {self.name} to {evolution[2]}.")
                break

    def synergy_effect(self, other_trait: 'Trait') -> Optional[str]:
        """
        Check if this trait synergizes with another trait.

        Parameters:
        - other_trait (Trait): Another trait object to compare against.

        Returns:
        - str: A description of the synergy effect, if one exists.
        """
        for synergy in TRAIT_SYNERGIES:
            if (self.name, other_trait.name) in synergy[0]:
                return synergy[1]  # Return the synergy effect description
        return None


class Personalitiy:
    def __init__(self, age_group, traits=None):
        """
        Initialize a Personality object.

        Parameters:
        - age_group (str): The current age group of the character.
        - traits (dict): A dictionary of traits assigned to the character, organized by trait category.
        """
        self.age_group = age_group
        self.traits = traits

    def generate(self):
        """
        Generate traits for a character based on their age group.

        This function selects traits from the predefined TRAITS list (positive, neutral, and negative)
        for each trait category available to the given age group.

        Returns:
        - dict: A dictionary of generated traits organized by trait category.
        """
        traits = {}
        for category in PERSONALITY_CATAGORIES[self.age_group]:
            traits[category] = random.choice(
                list(TRAITS[category]["positive"]) +
                list(TRAITS[category]["neutral"]) +
                list(TRAITS[category]["negative"])
            )
        return traits

    def evolve_traits(self):
        """
        Evolve all traits for the current age group.

        This function iterates through all the traits a character has and checks if they can evolve
        based on the current age group. If they can, they are updated accordingly.
        """
        for category, trait in self.traits.items():
            trait_instance = Trait(trait, self.age_group, category)
            trait_instance.evolve(self.age_group)
            self.traits[category] = trait_instance.name

    def check_synergy(self, other):
        """
        Check for synergy between the character's traits.

        This function compares each trait with every other trait to see if any synergies exist,
        and returns the synergy results.

        Returns:
        - list: A list of synergy effect descriptions.
        """
