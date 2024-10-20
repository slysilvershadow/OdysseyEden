# constants.py
HOUR_LEN = 60
DAY_LEN = 24
WEEK_LEN = 10
MONTH_LEN = 30
YEAR_LEN = 10

MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

MONTH_NAMES = ['Brigide', 'Imbolka', 'Floralis', 'Lithara', 'Heliax', 'Aestium', 'Mabonel', 'Ceresio', 'Yulith', 'Hibernis']
DAY_NAMES = ['Restony', 'Serement', 'Chronesis', 'Tempetude', 'Solament', 'Helioris', 'Duratonis', 'Resporal', 'Sabbathal', 'Noctitude']

# Character Needs
MAX_HUNGER = 100
MAX_THIRST = 100
MAX_ENERGY = 100
MAX_SOCIAL = 100
MAX_RELIEF = 100
MAX_CLEANLINESS = 100
MAX_COMFORT = 100
MAX_SAFETY = 100
MAX_HEALTH = 100

MIN_HUNGER = 0
MIN_THIRST = 0
MIN_ENERGY = 0
MIN_SOCIAL = 0
MIN_RELIEF = 0
MIN_CLEANLINESS = 0
MIN_COMFORT = 0
MIN_SAFETY = 0
MIN_HEALTH = 0

# Decay rates
HUNGER_DECAY = 2  # 2 points every in-game hour
THIRST_DECAY = 3  # 3 points every in-game hour
ENERGY_DECAY = 1  # 1 point every in-game hour
SOCIAL_DECAY = 1  # 1 point every in-game hour
RELIEF_DECAY = 2  # 2 points every in-game hour
CLEANLINESS_DECAY = 0.5  # 0.5 points every in-game hour
COMFORT_DECAY = 1  # 1 point every in-game hour
SAFETY_DECAY = 0.2  # 0.2 points every in-game hour
HEALTH_DECAY = 0.1  # 0.1 points every in-game hour

# Character Traits
SEX = ['x', 'y']
GENDER = ['masc', 'fem', 'androgynous']
TONE = ['pale', 'medium', 'tan', 'dark', 'deep']
UNDERTONE = ['warm', 'neutral', 'cool']
HEIGHT = ['short', 'average', 'tall']
BSHAPE = ['slim', 'average', 'athletic', 'curvy']
BSIZE = ['small', 'medium', 'large']
HCOLOR = ['black', 'brown', 'blonde', 'ginger']
HTEXT = ['straight', 'wavy', 'curly']
ESHAPE = ['round', 'almond', 'upturned', 'downturned', 'hooded']
ECOLOR = ['brown', 'hazel', 'green', 'blue', 'grey']
NPROFILE = ['small', 'medium', 'tall']
NSHAPE = ['refined', 'hero', 'soft', 'perky', 'dainty', 'strong', 'bulb']
MSHAPE = ['thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped']
RSHAPE = ['round', 'pointed']
RSIZE = ['small', 'medium', 'large']


RESPONSES = ['recpetive', 'motive', 'apprehensive', 'refusal']

AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}

BASE_STATS = {
            "Stamina": 10,
            "Strength": 10,
            "Dexterity": 10,
            "Perception": 10,
            "Willpower": 10
}

SKILLS = [
    'foraging', 'hunting', 'fishing', 'cooking', 'fire-making', 'shelter-building', 'farming', 'tool crafting', 'animal husbandry', 
    'melee', 'archery', 'defense', 'tactics', 'martial arts', 
    'woodworking', 'stoneworking', 'metalworking', 'textile crafting', 'pottery', 'building', 'leatherworking',
    'painting', 'writing', 'sculpting', 'music',
    'bartering', 'leadership', 'teaching', 'diplomacy','persuasion',
    'herbalism', 'first aid', 'surgery', 'midwifery', 'spiritual healing',
    'meditation', 'philosophy', 'spiritual leadership',
    'navigation', 'cartography', 'swimming', 'climbing',
    'cleaning', 'child rearing', 'clothing maintenance',
    'elemental', 'divination', 'alchemy', 'enchanting'
]

SKILLS_GROUPS = {
    'survival' : [SKILLS[0], SKILLS[1], SKILLS[2], SKILLS[3], SKILLS[4], SKILLS[5], SKILLS[6], SKILLS[7], SKILLS[8]], 
    'combat' : [SKILLS[9], SKILLS[10], SKILLS[11], SKILLS[12], SKILLS[13]],
    'crafting' : [SKILLS[14], SKILLS[15], SKILLS[16], SKILLS[17], SKILLS[18], SKILLS[19], SKILLS[20]],
    'artisan' :  [SKILLS[21], SKILLS[22], SKILLS[23], SKILLS[24]],
    'communication' : [SKILLS[25], SKILLS[26], SKILLS[27], SKILLS[28], SKILLS[29]],
    'healing' : [SKILLS[30], SKILLS[31], SKILLS[32], SKILLS[33], SKILLS[34]],
    'mental' : [SKILLS[35], SKILLS[36], SKILLS[37]],
    'exploration' : [SKILLS[38], SKILLS[39], SKILLS[40], SKILLS[41]],
    'domestic' : [SKILLS[42], SKILLS[43], SKILLS[44]],
    'magic' : [SKILLS[45], SKILLS[46], SKILLS[47], SKILLS[48]]
}

SKILL_STAT_RELATIONS = [
    [SKILLS_GROUPS[0], BASE_STATS['Stamina'], BASE_STATS['Strength']],
    [SKILLS_GROUPS[1], BASE_STATS['Strength'], BASE_STATS['Dexterity']],
    [SKILLS_GROUPS[2], BASE_STATS['Strength'], BASE_STATS['Perception']],
    [SKILLS_GROUPS[3], BASE_STATS['Stamina'], BASE_STATS['Dexterity']],
    [SKILLS_GROUPS[4], BASE_STATS['Perception'], BASE_STATS['Willpower']],
    [SKILLS_GROUPS[5], BASE_STATS['Stamina'], BASE_STATS['Perception']],
    [SKILLS_GROUPS[6], BASE_STATS['Willpower'], BASE_STATS['Perception']],
    [SKILLS_GROUPS[7], BASE_STATS['Dexterity'], BASE_STATS['Willpower']],
    [SKILLS_GROUPS[8], BASE_STATS['Stamina'], BASE_STATS['Willpower']],
    [SKILLS_GROUPS[9], BASE_STATS['Dexterity'], BASE_STATS['Willpower']],
}

SKILL_REQUIREMENTS = {
    'survival': ['sticks'],
    'combat': ['spear'],
    'crafting': ['crafting_table'],
    'artisan': ['artisans_workbench'],
    'communication': [],
    'healing': ['spindel', 'loom', 'lifespring fern'],
    'mental': [],
    'exploration': [],
    'domestic': ['shelter'],
    'magic': ['tomb']
}
