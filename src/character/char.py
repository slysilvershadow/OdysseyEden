import random
from src.utils import constants as con
from src.utils import constants as con
import genes
import needs

class Character:
    def __init__(self):
        self.id = uuid.uuid4()
		self.components = {}
		
	def add_component(self, component):
		self.components[type(component)] = component
		return self
		
class Looks:
	def __init__(self, sprite):
		self.sprite = sprite
		
class Stats:
	def __init__(self, base_stats):
		self.base_stats = base_stats
		self.advanced_stats = {}
		
class Skills:
	def __init__(self, skills):
		self.skills = skills
		
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

class SkillSys:
	def update(self, entities):
		for entity in entities:
            skills_comp = entity.get_component(SkillsComponent)
            stats_comp = entity.get_component(StatsComponent)
            if skills_comp and stats_comp:
                for skill in skills_comp.skills:
                    levels_gained = skill.level_up()
                    skills_comp.improve_related_stats(skill, levels_gained)