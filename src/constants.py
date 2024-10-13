# Time and Calendar
HOUR_LEN = 60
DAY_LEN = 24
WEEK_LEN = 10
MONTH_LEN = 30
YEAR_LEN = 10

MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

MONTH_NAMES = ["Brigide", "Imbolka", "Floralis", "Lithara", "Heliax", "Aestium", "Mabonel", "Ceresio", "Yulith", "Hibernis"]
DAY_NAMES = ["Restony", "Serement", "Chronesis", "Tempetude", "Solament", "Helioris", "Duratonis", "Resporal", "Sabbathal", "Noctitude"]

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

# Decay rates (add values here for how fast each need decays over time)
HUNGER_DECAY = None
THIRST_DECAY = None
ENERGY_DECAY = None
SOCIAL_DECAY = None
RELIEF_DECAY = None
CLEANLINESS_DECAY = None
COMFORT_DECAY = None
SAFETY_DECAY = None
HEALTH_DECAY = None

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

# Temperament System (opposites mapped)
TEMPERAMENTS = {
    'sanguine': {'max': 10, 'min': 0, 'opposite': 'melancholic'},
    'choleric': {'max': 10, 'min': 0, 'opposite': 'phlegmatic'},
    'melancholic': {'max': 10, 'min': 0, 'opposite': 'sanguine'},
    'phlegmatic': {'max': 10, 'min': 0, 'opposite': 'choleric'}
}

# MBTI System (opposites mapped)
MBTI = {
    'introverted': {'max': 10, 'min': 0, 'opposite': 'extroverted'},
    'extroverted': {'max': 10, 'min': 0, 'opposite': 'introverted'},
    'sensory': {'max': 10, 'min': 0, 'opposite': 'intuitive'},
    'intuitive': {'max': 10, 'min': 0, 'opposite': 'sensory'},
    'feeling': {'max': 10, 'min': 0, 'opposite': 'thinking'},
    'thinking': {'max': 10, 'min': 0, 'opposite': 'feeling'},
    'perceiving': {'max': 10, 'min': 0, 'opposite': 'judging'},
    'judging': {'max': 10, 'min': 0, 'opposite': 'perceiving'}
}

AGES = {
    'baby' : {
        'years' : 1,
        'new_traits' : 0,
        'evo_traits' : 0,
        'pos_traits' : None,
        'mbti' : False,
        'temperament' : False,
        'pos_skills' : 0,
        'skills' : None
    },
    'toddler' : {
    	'years' : 2,
        'new_traits' : 2,
        'evo_traits' : 0,
        'pos_traits' : {
            'positive' : ['curious', 'playful', 'affectionate', 'imaginative'],
            'neutral' : ['innocent', 'restless', 'impulsive', 'sensitive'],
            'negative' : ['stubborn', 'whiny', 'tantrum-prone', 'easily frightened']
        },
        'mbti' : True or False,
        'temperament' : True or False,
        'pos_skills' : None,
        'skills' : None
    },
    'child' : {
        'years' : 4,
        'new_traits' : 2,
        'evo_traits' : 0,
        'pos_traits' : {
            'positive' : ['sociable', 'caring', 'creative', 'adventurous', 'inquisitive'],
            'neutral' : ['impressionable', 'playful', 'overly honest', 'curious'],
            'negative' : ['self-centered', 'easily distracted', 'fearful of new things', 'clingy']
        },
        'mbti' : True or False,
        'temperament' : True or False,
        'pos_skills' : None,
        'skills' : None
    },
    'teenager' : {
        'years' : 3,
        'new_traits' : 1,
        'evo_traits' : 0,
        'pos_traits' : {
            'positive' : ['rebellious', 'empathetic', 'optimistic', 'determined', 'independent', 'thoughtful'],
            'neutral' : ['moody', 'insecure', 'impulsive', 'idealistic'],
            'negative' : ['overly critical', 'defiant', 'withdrawn', 'self-destructive']
        },
        'mbti' : True or False,
        'temperament' : True or False,
        'pos_skills' : None,
        'skills' : None
    },
    'young adult' : {
        'years' : 12,
        'new_traits' : 0,
        'evo_traits' : 0,
        'pos_traits' : {
            'positive' : ['ambitious', 'resilient', 'open-minded', 'socially aware', 'adventurous'],
            'neutral' : ['restless', 'anxious', 'eager to please', 'exploratory'],
            'negative' : ['impulsive', 'overwhelemed','indesisive', 'narrow-minded']
        },
        'mbti' : True or False,
        'temperament' : True or False,
        'pos_skills' : None,
        'skills' : None
    },
    'adult' : {
        'years' : 30,
        'new_traits' : 0,
        'evo_traiits' : 0,
        'pos_traits' : {
            'positive' : ['responsible', 'wise', 'supportive', 'mentor-like', 'pragmatic'],
            'neutral' : ['cynical', 'routine-oriented', 'pensive', 'realistic'],
            'negative' : ['stressed', 'overbearing', 'complacent', 'resentful']
        },
        'mbti' : True or False,
        'temperament' : True or False,
        'pos_skills' : None,
        'skills' : None
    },
    'elder' : {
        'years' : 20,
        'new_traits' : 0,
        'evo_traits' : 0,
        'pos_traits' : {
            'positive' : ['reflective', 'nuturing', 'wise mentor', 'storyteller', 'caring'],
            'neutral' : ['melancholic', 'forgetful', 'pensive', 'inquisitive'],
            'negative' : ['grumpy', 'set in their ways', 'withdrawn', 'skeptical']
        },
        'mbti' : True or False,
        'temperament' : True or False,
        'pos_skills' : None,
        'skills' : None
    }
} 

