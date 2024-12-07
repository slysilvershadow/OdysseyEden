# skills.py

class Skill:
    def __init__(self, name: str, group: str, lvl: int = 0, exp: float = 0.0, max_lvl: int = 20):
        """
        Initialize a skill object
        Parameters:
            - name (str): The name of the skill.
        - group (str): The catagory that the skill belongs to.
        - lvl (int): The current level of the skill.
        - exp (float): The current experience points for the skill.
        - max_lvl (int): The maximum level a skill can reach.
        """
        self.name: str = name
        self.lvl: int = lvl
        self.exp: float = exp
        self.max_lvl: int = max_lv
    def add_exp(self, amount: float) -> float:
        """
        Add experience points and check if the skill should level up
        Parameters:
            - amount (float): The amount of experience to add
        Returns:
            - float: The updated experience points.
        """
        self.exp += amount

        while self.exp < 0 and self.lvl > 0:
            self.exp += self.exp_to_next_lvl()
            self.lvl_down()

        while self.lvl < self.max_lvl and self.exp ≥ self.exp_to_next_lvl():
            self.exp -= self.exp_to_next_lvl()
            self.lvl_up()

        return self.exp
    
    def exp_to_next_lvl(self) -> int:
            return 100 * (self.lvl + 1)
    def lvl_up(self) -> None:
            if self.lvl < self.max_lvl:
                self.lvl += 1
            print(f"{self.name} leveled up to level {self.lvl}!")
    
    def lvl_down(self) -> None:
        	if self.lvl > 0:
        		self.lvl --= 1
    		print(f"{self.name} leveled down to level {self.lvl}!"

    


"""Survival Skills
#These skills help characters meet their basic needs and thrive in their environment:
Foraging: Collecting edible plants, fruits, and herbs from the environment.
Hunting: Tracking and killing animals for food and resources (weapons or traps could enhance this).
Fishing: Using basic tools to catch fish from lakes, rivers, or oceans.
Cooking: Preparing food from foraged, hunted, or farmed ingredients (improves character satisfaction and hunger reduction).
Fire-making: Building and maintaining fires, essential for cooking, warmth, and safety.
Shelter-building: Constructing or upgrading homes and structures for the tribe.
Farming: Growing crops and tending to animals, providing a sustainable food supply.
Tool Crafting: Creating and maintaining tools and weapons from available materials.
Animal Husbandry: Raising and caring for livestock, with a focus on breeding, feeding, and domesticating wild animals.
2. Combat Skills
As conflict may arise in tribal or wild settings, combat is a key skill set:

Melee Combat: Proficiency in close-range weapons like swords, spears, or clubs.
Archery: Mastery of bows for hunting or defending the tribe from a distance.
Defense: Learning defensive tactics to block attacks, dodge, or use shields.
Tactics: Strategic planning in battles, coordinating attacks, or leading groups during combat.
Martial Arts: Hand-to-hand combat skills, useful when weapons aren’t available.
3. Crafting & Construction Skills
These skills allow for development of the environment, from personal items to entire settlements:

Woodworking: Crafting objects like furniture, tools, or buildings from wood.
Stoneworking: Building with stone or creating advanced tools and structures.
Metalworking: Forging weapons, tools, or armor from metals (an advanced skill).
Textile Crafting: Creating clothes and other fabric items (using wool, plant fibers, etc.).
Pottery: Crafting clay-based items, which can be practical (containers) or decorative.
Building: Designing and constructing buildings and other larger structures.
Leatherworking: Using animal hides to make clothing, armor, and various accessories.
4. Artisan Skills
These skills focus on creativity and cultural growth:

Painting: Creating art to beautify surroundings or communicate stories (on walls, pottery, etc.).
Writing: Composing stories, records, or spells (depending on how advanced the culture is).
Sculpting: Crafting statues or other items from wood, stone, or clay to express creativity or honor the tribe’s beliefs.
Music: Playing instruments or singing to boost morale or tell stories.
5. Social & Communication Skills
These skills are vital for building relationships within the tribe and beyond:

Bartering: Negotiating trades with other tribes or within the community.
Leadership: Inspiring others, making decisions for the tribe, and managing group morale.
Teaching: Passing down knowledge to younger generations, allowing skills to propagate within the tribe.
Diplomacy: Managing relationships with other tribes, handling alliances or conflicts peacefully.
Persuasion: Convincing others in social situations, influencing tribe decisions, or negotiating.
6. Medical & Healing Skills
These skills ensure the health and well-being of the tribe:

Herbalism: Using plants and herbs to create remedies and potions for healing.
First Aid: Basic knowledge of tending to wounds, treating injuries, and stabilizing others.
Surgery: More advanced medical techniques (reserved for experienced healers).
Midwifery: Assisting with childbirth and caring for mothers and infants.
Spiritual Healing: Depending on the culture, using rituals or spiritual guidance to heal emotional or spiritual wounds.
7. Mental & Spiritual Skills
These skills contribute to personal growth, wisdom, and understanding of the world:

Meditation: Calming the mind, reducing stress, and potentially increasing wisdom.
Philosophy: Understanding and debating the world’s truths, contributing to the tribe’s moral compass.
Spiritual Leadership: Guiding the tribe through religious or spiritual rituals, strengthening cultural identity.
8. Exploration & Navigation Skills
For navigating and understanding the broader game world:

Navigation: Finding paths through wilderness or biomes, potentially using stars or natural markers.
Cartography: Creating maps of explored areas for future reference and use by the tribe.
Swimming: Safely crossing bodies of water, either for exploration or survival.
Climbing: Scaling cliffs, trees, or structures for exploration or defense.
9. Household & Domestic Skills
For keeping homes and personal lives in order:

Cleaning: Maintaining personal and communal spaces (ties into your “Cleanliness” need).
Child-rearing: Caring for and educating the next generation (important for long-term tribe survival).
Clothing Maintenance: Repairing worn clothes or improving clothing items.
10. Magical Skills (if applicable)
If magic exists in the game’s world:

Elemental Magic: Control over natural forces like fire, water, earth, and air.
Divination: Seeing into the future or interpreting signs for guidance.
Alchemy: Mixing potions or transmuting materials to change their properties.
Enchanting: Adding magical properties to items like weapons or clothing."""
