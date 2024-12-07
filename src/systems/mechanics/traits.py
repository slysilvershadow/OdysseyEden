from src.components.traits import CATEGORIES_PER_AGE, TRAIT_EVOLUTIONS, TRAIT_SYNERGIES
from src.utils.constants import AGES, TRAITS

class TraitSystem:
    def __init__(self):
        self.categories_per_age = CATEGORIES_PER_AGE
        self.trait_evolutions = TRAIT_EVOLUTIONS
        self.trait_synergies = TRAIT_SYNERGIES
        
    def get_available_traits(self, age):
        return self.categories_per_age.get(age, [])
        
    def evolve_traits(self, current_traits, new_age):
        evolved_traits = []
        for trait in current_traits:
            for old_trait, new_trait, evolution_age in self.trait_evolutions:
                if trait == old_trait and new_age == evolution_age:
                    evolved_traits.append(new_trait)
                    break
            else:
                evolved_traits.append(trait)
        return evolved_traits
                
    def get_trait_synergies(self, traits):
        active_synergies = []
        for trait_pair, effect in self.trait_synergies:
            if all(trait in traits for trait in trait_pair):
                active_synergies.append((trait_pair, effect))
        return active_synergies

    def generate_initial_traits(self):
        initial_traits = []
        infant_categories = self.categories_per_age[AGES['infant']]
        
        for category in infant_categories:
            trait_pool = (
                category['positive'] +
                category['neutral'] +
                category['negative']
            )
            initial_traits.append(random.choice(trait_pool))
        return initial_traits
    
    def calculate_trait_compatibility(self, traits_a, traits_b):
        compatibility_score = 0
        
        for trait_a in traits_a:
            for trait_b in traits_b:
                # Check for direct synergies
                for pair, _ in self.trait_synergies:
                    if (trait_a, trait_b) == pair or (trait_b, trait_a) == pair:
                        compatibility_score += 2
                
                # Check for trait category alignment
                if self._are_traits_aligned(trait_a, trait_b):
                    compatibility_score += 1
                    
        return compatibility_score
    
    def _are_traits_aligned(self, trait_a, trait_b):
        # Helper method to check if traits are from same category/polarity
        for category in TRAITS.values():
            if (trait_a in category['positive'] and trait_b in category['positive']) or \
               (trait_a in category['negative'] and trait_b in category['negative']) or \
               (trait_a in category['neutral'] and trait_b in category['neutral']):
                return True
        return False
