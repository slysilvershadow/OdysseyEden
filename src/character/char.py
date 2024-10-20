import pyglet
import random
from src.utils import constants as con
import genes
import needs

class Character(pyglet.sprite.Sprite):
    def __init__(self, **kwargs):
        pass
      
    def improve_related_stats(self, skill: Skill, levels_gained: int):

        if skill.group in con.SKILL_STAT_RELATIONS:
            related_stats = con.SKILL_STAT_RELATIONS[skill.group]
            for stat in related_stats:
                self.base_stats[stat] += levels_gained * 0.1  # Adjust this multiplier as needed
                self.update_advanced_stats()
                print(f"Improved {', '.join(related_stats)} from leveling up {skill.name}!")
                # Small chance to improve a random stat
        if random.random() < 0.05:  # 5% chance
            random_stat = random.choice(list(self.base_stats.keys()))
            self.base_stats[random_stat] += levels_gained * 0.05
            print(f"Lucky! Also improved {random_stat} a bit.")
