# constants.py

#Worlds
BIOMES = []

#Time
HOUR_LEN = 60
DAY_LEN = 24
WEEK_LEN = 10
MONTH_LEN = 30
YEAR_LEN = 10

MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

MONTH_NAMES = ['Brigide', 'Imbolka', 'Floralis', 'Lithara',
               'Heliax', 'Aestium', 'Mabonel', 'Ceresio', 'Yulith', 'Hibernis']
DAY_NAMES = ['Restony', 'Serement', 'Chronesis', 'Tempetude', 'Solament',
             'Helioris', 'Duratonis', 'Resporal', 'Sabbathal', 'Noctitude']

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

# Default Decay rates
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

AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}

TRAITS = {
    'temperament': {
        'positive': [
            'easy-going',
            'adaptable',
            'content',
            'cheerful',
            'calm'
        ],
        'neutral': [
            'active',
            'regular',
            'slow-to-warm-up',
            'moderate',
            'observant'
        ],
        'negative': [
            'fussy',
            'irritable',
            'unpredictable',
            'restless',
            'overactive'
        ]
    },
    'socialization': {
        'positive': [
            'sociable',
            'playful',
            'affectionate',
            'friendly',
            'outgoing'
        ],
        'neutral': [
            'observant',
            'independent',
            'cautious',
            'curious',
            'mellow'
        ],
        'negative': [
            'clingy',
            'irritable',
            'withdrawn',
            'hyperactive',
            'impulsive'
        ]
    },
    'emotional': {
        'positive': [
            'cheerful',
            'passionate',
            'optimistic',
            'joyful',
            'hopeful'
        ],
        'neutral': [
            'sensitive',
            'calm',
            'reflective',
            'balanced',
            'realistic'
        ],
        'negative': [
            'moody',
            'anxious',
            'gloomy',
            'aggressive',
            'doubtful'
        ]
    },
    'interaction': {
        'positive': [
            'cooperative',
            'empathetic',
            'supportive',
            'generous',
            'trustworthy'
        ],
        'neutral': [
            'reserved',
            'independent',
            'adaptable',
            'neutral',
            'pragmatic'
        ],
        'negative': [
            'shy',
            'confrontational',
            'manipulative',
            'aloof',
            'dismissive'
        ]
    },
    'cognition': {
        'positive': [
            'curious',
            'diligent',
            'creative',
            'inquisitive',
            'motivated'
        ],
        'neutral': [
            'practical',
            'analytical',
            'intuitive',
            'theoretical',
            'exploratory'
        ],
        'negative': [
            'distracted',
            'stubborn',
            'uncritical',
            'complacent',
            'disinterested'
        ]
    },
    'identity': {
        'positive': [
            'confident',
            'principled',
            'open-minded',
            'self-aware',
            'authentic'
        ],
        'neutral': [
            'questioning',
            'experimental',
            'idealistic',
            'reflective',
            'curious'
        ],
        'negative': [
            'insecure',
            'conformist',
            'rebellious',
            'conflicted',
            'doubtful'
        ]
    },
    'ambition': {
        'positive': [
            'ambitious',
            'dedicated',
            'innovative',
            'goal-oriented',
            'driven'
        ],
        'neutral': [
            'flexible',
            'specialized',
            'risk-taking',
            'pragmatic',
            'adaptable'
        ],
        'negative': [
            'unmotivated',
            'workaholic',
            'indecisive',
            'complacent',
            'disengaged'
        ]
    },
    'morals': {
        'positive': [
            'honest',
            'compassionate',
            'resilient',
            'fair-minded',
            'generous'
        ],
        'neutral': [
            'traditional',
            'pragmatic',
            'individualistic',
            'balanced',
            'neutral'
        ],
        'negative': [
            'materialistic',
            'judgmental',
            'hedonistic',
            'selfish',
            'cynical'
        ]
    },
    'perspective': {
        'positive': [
            'wise',
            'content',
            'grateful',
            'optimistic',
            'hopeful'
        ],
        'neutral': [
            'philosophical',
            'nostalgic',
            'accepting',
            'realistic',
            'pragmatic'
        ],
        'negative': [
            'cynical',
            'regretful',
            'bitter',
            'despondent',
            'resentful'
        ]
    },
    'legacy': {
        'positive': [
            'mentoring',
            'philanthropic',
            'inspiring',
            'guiding',
            'visionary'
        ],
        'neutral': [
            'reflective',
            'private',
            'traditional',
            'conservative',
            'practical'
        ],
        'negative': [
            'disengaged',
            'controlling',
            'resentful',
            'manipulative',
            'detached'
        ]
    }
}

STATS = {
    'core': {
        'stamina': int,
        'strength': int,
        'dexterity': int,
        'perception': int,
        'willpower': int},
    'advanced': {
        'endurance': int,
        'prowess': int,
        'finess': int,
        'conviction': int,
        'vitality': int}
}

SKILLS = {
    'survival': ['foraging', 'hunting', 'fishing', 'cooking', 'fire-making', 'shelter-building', 'farming', 'tool crafting', 'animal husbandry'],
    'combat': ['melee', 'archery', 'defense', 'tactics', 'martial arts'],
    'crafting': ['woodworking', 'stoneworking', 'metalworking', 'textile crafting', 'pottery', 'building', 'leatherworking'],
    'artisan':  ['painting', 'writing', 'sculpting', 'music'],
    'communication': ['bartering', 'leadership', 'teaching', 'diplomacy', 'persuasion'],
    'healing': ['herbalisim', 'first aid', 'surgery', 'midwifery', 'spiritual healing'],
    'mental': ['meditation', 'philosophy', 'spiritual leadership'],
    'exploration': ['navigation', 'cartography', 'swimming', 'climbing'],
    'domestic': ['cleaning', 'child rearing', 'clothing maintenance'],
    'magic': ['elemental', 'divination', 'alchemy', 'enchanting']
}

#Possible responses from ai
RESPONSES = ['receptive', 'motive', 'apprehensive', 'refusal']
