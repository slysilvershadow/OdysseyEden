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

PERSONALITY_CATAGORIES = {
    'infant': ['temperament'],
    'sprout': ['temperament', 'socialization'],
    'youth': ['emotional', 'interaction', 'cognition'],
    'adolescent': ['emotional', 'interaction', 'cognition', 'identity'],
    'prime': ['emotional', 'interaction', 'ambition', 'morals'],
    'mature': ['emotional', 'interaction', 'ambition', 'morals', 'perspective'],
    'sage': ['emotional', 'interaction', 'morals', 'perspective', 'legacy']
}

TRAITS = {
    'temperament': {
        'postitive': ['easy-going', 'adaptable', 'content', 'cheerful', 'calm'],
        'neutral': ['active', 'regular', 'slow-to-warm-up', 'moderate', 'observant'],
        'negative': ['fussy', 'irritable', 'unpredictable', 'restless', 'overactive']
    }, 
    'socialization': {
        'postitive': ['sociable', 'playful', 'affectionate', 'friendly', 'engaging'],
        'neutral': ['observant', 'independent', 'cautious', 'curious', 'mellow'],
        'negative': ['clingy', 'aggressive', 'withdrawn', 'hyperactive', 'impulsive']
    },
    'emotional': {
        'postitive': ['cheerful', 'calm', 'optimistic', 'joyful', 'hopeful'],
        'neutral': ['sensitive', 'passionate', 'reflective', 'balanced', 'realistic'],
        'negative': ['moody', 'anxious', 'pessimistic', 'irritable', 'doubtful']
    },
    'interaction': {
        'positive': ['friendly', 'cooperative', 'empathetic', 'supportive', 'generous'],
        'neutral': ['reserved', 'independent', 'adaptable', 'neutral', 'pragmatic'],
        'negative': ['shy', 'confrontational', 'manipulative', 'aloof', 'dismissive']
    },
    'cognition': {
        'positive': ['curious', 'diligent', 'creative', 'inquisitive', 'motivated'],
        'neutral': ['practical', 'analytical', 'intuitive', 'theoretical', 'exploratory'],
        'negative': ['distracted', 'stubborn', 'uncritical', 'complacent', 'disinterested']
    },
    'identity': {
        'positive': ['confident', 'principled', 'open-minded', 'self-aware', 'authentic'],
        'neutral': ['questioning', 'experimental', 'idealistic', 'reflective', 'curious'],
        'negative': ['insecure', 'conformist', 'rebellious', 'conflicted', 'doubtful']
    }, 
    'ambition': {
        'positive': ['ambitious', 'dedicated', 'innovative', 'goal-oriented', 'driven'],
        'neutral': ['flexible', 'specialized', 'risk-taking', 'pragmatic', 'adaptable'],
        'negative': ['unmotivated', 'workaholic', 'indecisive', 'complacent', 'disengaged']
    },
    'morals': {
        'positive': ['honest', 'compassionate', 'resilient', 'fair-minded', 'generous'],
        'neutral': ['traditional', 'pragmatic', 'individualistic', 'balanced', 'neutral'],
        'negative': ['materialistic', 'judgmental', 'hedonistic', ' selfish', 'cynical']
    },
    'perspective': {
        'positive': ['wise', 'content', 'grateful', 'optimistic', 'hopeful'],
        'neutral': ['philosophical', 'nostalgic', 'accepting', 'realistic', 'pragmatic'],
        'negative': ['cynical', 'regretful', 'bitter', 'pessimistic', 'resentful']
    },
    'legacy': {
        'positive': ['mentoring', 'philanthropic', 'inspiring', 'guiding', 'visionary'],
        'neutral': ['reflective', 'private', 'traditional', 'conservative', 'practical'],
        'negative': ['disengaged', 'controlling', 'resentful', 'manipulative', 'detached']
    }
}

TRAIT_EVOLUTIONS = [
    ("Curious", "Inquisitive", "Teen"),
    ("Inquisitive", "Analytical", "Young Adult"),
    ("Cheerful", "Optimistic", "Teen"),
    ("Optimistic", "Resilient", "Adult"),
    ("Friendly", "Empathetic", "Teen"),
    ("Empathetic", "Compassionate", "Adult"),
    ("Diligent", "Dedicated", "Young Adult"),
    ("Dedicated", "Ambitious", "Adult"),
    ("Creative", "Innovative", "Young Adult"),
    ("Innovative", "Visionary", "Adult"),
    ("Shy", "Reserved", "Teen"),
    ("Reserved", "Independent", "Adult"),
    ("Moody", "Passionate", "Teen"),
    ("Passionate", "Intense", "Adult"),
    ("Anxious", "Sensitive", "Teen"),
    ("Sensitive", "Reflective", "Adult"),
    ("Pessimistic", "Cynical", "Teen"),
    ("Cynical", "Resentful", "Adult"),
    ("Conformist", "Traditional", "Adult"),
    ("Rebellious", "Nonconformist", "Adult"),
    ("Insecure", "Self-doubting", "Adult"),
    ("Stubborn", "Unyielding", "Teen"),
    ("Uncritical", "Naive", "Teen"),
    ("Distracted", "Disorganized", "Teen"),
    ("Manipulative", "Deceptive", "Adult"),
    ("Confrontational", "Aggressive", "Adult"),
    ("Workaholic", "Obsessive", "Adult"),
    ("Indecisive", "Hesitant", "Adult"),
    ("Materialistic", "Greedy", "Adult"),
    ("Judgmental", "Critical", "Adult"),
    ("Hedonistic", "Self-indulgent", "Adult"),
    ("Cynical", "Jaded", "Elder"),
    ("Regretful", "Remorseful", "Elder"),
    ("Bitter", "Resentful", "Elder"),
    ("Disengaged", "Detached", "Elder"),
    ("Controlling", "Manipulative", "Elder"),
    ("Resentful", "Vindictive", "Elder"),
    ("Mentoring", "Guiding", "Elder"),
    ("Philanthropic", "Altruistic", "Elder"),
    ("Inspiring", "Visionary", "Elder"),
    ("Reflective", "Introspective", "Elder"),
    ("Private", "Reserved", "Elder"),
    ("Traditional", "Conservative", "Elder"),
    ("Adaptable", "Easy-going", "Toddler"),
    ("Engaging", "Sociable", "Child"),
    ("Hopeful", "Joyful", "Teen"),
    ("Self-aware", "Confident", "Young Adult"),
    ("Goal-oriented", "Young Adult", "Ambitious", "Adult"),
    ("Generous", "Compassionate", "Elder"),
    ("Pragmatic", "Neutral", "Young Adult"),
    ("Mellow", "Balanced", "Teen"),
    ("Reflective", "Philosophical", "Adult"),
    ("Authentic", "Principled", "Adult"),
]

TRAIT_SYNERGIES = [
    (("Curious", "Inquisitive"), "Enhances learning speed for knowledge-seeking skills"),
    (("Cheerful", "Optimistic"), "Boosts creativity-related skill gains"),
    (("Friendly", "Empathetic"), "Improves social relationships and diplomacy"),
    (("Diligent", "Dedicated"), "Increases productivity and work efficiency"),
    (("Creative", "Innovative"), "Enhances problem-solving and critical thinking"),
    (("Shy", "Reserved"), "Reduces social anxiety and improves self-confidence"),
    (("Moody", "Passionate"), "Increases emotional intensity and creativity"),
    (("Anxious", "Sensitive"), "Improves emotional intelligence and empathy"),
    (("Pessimistic", "Cynical"), "Increases critical thinking and skepticism"),
    (("Conformist", "Traditional"), "Improves social standing and reputation"),
    (("Rebellious", "Nonconformist"), "Increases independence and self-reliance"),
    (("Insecure", "Self-doubting"), "Improves self-awareness and personal growth"),
    (("Stubborn", "Unyielding"), "Increases determination and perseverance"),
    (("Uncritical", "Naive"), "Improves open-mindedness and adaptability"),
    (("Distracted", "Disorganized"), "Reduces procrastination and improves time management"),
    (("Manipulative", "Deceptive"), "Increases persuasion and negotiation skills"),
    (("Confrontational", "Aggressive"), "Increases assertiveness and conflict resolution skills"),
    (("Workaholic", "Obsessive"), "Increases productivity and work efficiency"),
    (("Indecisive", "Hesitant"), "Improves decision-making and risk-taking"),
    (("Materialistic", "Greedy"), "Increases wealth and material possessions"),
    (("Judgmental", "Critical"), "Increases critical thinking and discernment"),
    (("Hedonistic", "Self-indulgent"), "Increases pleasure and enjoyment"),
    (("Cynical", "Jaded"), "Increases skepticism and critical thinking"),
    (("Regretful", "Remorseful"), "Improves self-awareness and personal growth"),
    (("Bitter", "Resentful"), "Increases emotional intensity and motivation"),
    (("Disengaged", "Detached"), "Reduces emotional attachment and increases independence"),
    (("Controlling", "Manipulative"), "Increases persuasion and negotiation skills"),
    (("Resentful", "Vindictive"), "Increases motivation and drive"),
    (("Mentoring", "Guiding"), "Improves leadership and teaching skills"),
    (("Philanthropic", "Altruistic"), "Increases generosity and kindness"),
    (("Inspiring", "Visionary"), "Increases charisma and leadership skills"),
    (("Reflective", "Introspective"), "Improves self-awareness and personal growth"),
    (("Private", "Reserved"), "Reduces social anxiety and improves self-confidence"),
    (("Traditional", "Conservative"), "Improves social standing and reputation"),
    (("Adaptable", "Easy-going"), "Enhances flexibility and stress management"),
    (("Engaging", "Sociable"), "Boosts charisma and social influence"),
    (("Hopeful", "Joyful"), "Increases resilience and positivity"),
    (("Self-aware", "Confident"), "Enhances personal growth and self-acceptance"),
    (("Goal-oriented", "Ambitious"), "Increases focus and achievement"),
    (("Generous", "Compassionate"), "Strengthens community bonds and support"),
    (("Pragmatic", "Flexible"), "Improves problem-solving and adaptability"),
    (("Mellow", "Balanced"), "Enhances emotional stability and calmness"),
    (("Reflective", "Philosophical"), "Deepens understanding and wisdom"),
    (("Authentic", "Principled"), "Promotes integrity and trustworthiness"),
]
