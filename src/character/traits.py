from src.utils import constants as con
TRAITS = {
    '0temperament': {
        '0positive':('0easy-going', '1adaptable', '2content', '3cheerful', '4calm'),
        '1neutral': ('0active', '1regular', '2slow-to-warm-up', '3moderate', '4observant'),
        '2negative':('0fussy', '1irritable', '2unpredictable', '3restless', '4overactive')
    }, 
    '1socialization': {
        '0positive':('0sociable', '1playful', '2affectionate', '3friendly', '4engaging'),
        '1neutral': ('0observant', '1independent', '2cautious', '3curious', '4mellow'),
        '2negative':('0clingy', '1aggressive', '2withdrawn', '3hyperactive', '4impulsive')
    },
    '2emotional': {
        '0positive':('0cheerful', '1calm', '2optimistic', '3joyful', '4hopeful'),
        '1neutral': ('0sensitive', '1passionate', '2reflective', '3balanced', '4realistic'),
        '2negative':('0moody', '1anxious', '2pessimistic', '3irritable', '4doubtful')
    },
    '3interaction': {
        '0positive':('0friendly', '11cooperative', '2empathetic', '3supportive', '4generous'),
        '1neutral': ('0reserved', '11independent', '2adaptable', '3neutral', '4pragmatic'),
        '2negative':('0shy', '11confrontational', '2manipulative', '3aloof', '4dismissive')
    },
    '4cognition': {
        '0positive':('0curious', '11diligent', '2creative', '3inquisitive', '4motivated'),
        '1neutral': ('0practical', '11analytical', '2intuitive', '3theoretical', '4exploratory'),
        '2negative':('0distracted', '11stubborn', '2uncritical', '3complacent', '4disinterested')
    },
    '5identity': {
        '0positive':('0confident', '1principled', '2open-minded', '3self-aware', '4authentic'),
        '1neutral': ('0questioning', '1experimental', '2idealistic', '3reflective', '4curious'),
        '2negative':('0insecure', '1conformist', '2rebellious', '3conflicted', '4doubtful')
    },
    '6ambition': {
        '0positive':('0ambitious', '1dedicated', '2innovative', '3goal-oriented', '4driven'),
        '1neutral': ('0flexible', '1specialized', '2risk-taking', '3pragmatic', '4adaptable'),
        '2negative':('0unmotivated', '1workaholic', '2indecisive', '3complacent', '4disengaged')
    },
    '7morals': {
        '0positive':('0honest', '1compassionate', '2resilient', '3fair-minded', '4generous'),
        '1neutral': ('0traditional', '1pragmatic', '2individualistic', '3balanced', '4neutral'),
        '2negative':('0materialistic', '1judgmental', '2hedonistic', ' 3selfish', '4cynical')
    },
    '8perspective': {
        '0positive':('0wise', '1content', '2grateful', '3optimistic', '4hopeful'),
        '1neutral': ('0philosophical', '1nostalgic', '2accepting', '3realistic', '4pragmatic'),
        '2negative':('0cynical', '1regretful', '2bitter', '3pessimistic', '4resentful')
    },
    '9legacy': {
        '0positive':('0mentoring', '1philanthropic', '2inspiring', '3guiding', '4visionary'),
        '1neutral': ('0reflective', '1private', '2traditional', '3conservative', '4practical'),
        '2negative':('0disengaged', '1controlling', '2resentful', '3manipulative', '4detached')
    }
}

CATAGORIES_PER_AGE = {
    con.AGES[0]: (TRAITS[0]),
    con.AGES[1]: (TRAITS[0], TRAITS[1]),
    con.AGES[2]: (TRAITS[2], TRAITS[3], TRAITS[4]),
    con.AGES[3]: (TRAITS[2], TRAITS[3], TRAITS[4], TRAITS[5]),
    con.AGES[4]: (TRAITS[2], TRAITS[3], TRAITS[6], TRAITS[7]),
    con.AGES[5]: (TRAITS[2], TRAITS[3], TRAITS[6], TRAITS[7], TRAITS[8]),
    con.AGES[6]: (TRAITS[2], TRAITS[3], TRAITS[7], TRAITS[8], TRAITS[9])
}

TRAIT_EVOLUTIONS = [
    (TRAITS[0][0][0], TRAITS[0][0][1], AGES[1]),
    (TRAITS[1][0][0], TRAITS[1][0][1], AGES[2]),
    (TRAITS[2][0][0], TRAITS[2][0][2], AGES[3]),
    (TRAITS[2][0][1], TRAITS[2][0][2], AGES[3]),
    (TRAITS[2][1][1], TRAITS[2][1][2], AGES[3]),
    (TRAITS[2][2][0], TRAITS[2][1][1], AGES[3]),
    (TRAITS[2][2][1], TRAITS[2][1][0], AGES[3]),
    (TRAITS[2][2][2], TRAITS[8][2][0], AGES[3]),
    (TRAITS[3][0][0], TRAITS[3][0][2], AGES[3]),
    (TRAITS[3][2][0], TRAITS[3][1][0], AGES[3]),
    (TRAITS[4][0][0], TRAITS[4][0][1], AGES[3]),
    (TRAITS[4][0][1], TRAITS[4][1][1], AGES[4]),
    (TRAITS[4][2][0], TRAITS[4][2][4], AGES[3]),
    (TRAITS[4][2][1], TRAITS[4][2][2], AGES[3]),
    (TRAITS[4][2][2], TRAITS[4][2][3], AGES[3]),
    (TRAITS[4][0][1], TRAITS[6][0][1], AGES[4]),
    (TRAITS[4][0][2], TRAITS[6][0][2], AGES[4]),
    (TRAITS[4][1][0], TRAITS[4][1][1], AGES[4]),
    (TRAITS[5][0][0], TRAITS[5][0][1], AGES[4]),
    (TRAITS[2][0][2], TRAITS[7][0][2], AGES[5]),
    (TRAITS[2][1][0], TRAITS[8][1][0], AGES[5]),
    (TRAITS[2][1][1], TRAITS[2][1][2], AGES[5]),
    (TRAITS[3][0][2], TRAITS[7][0][0], AGES[5]),
    (TRAITS[3][1][0], TRAITS[5][1][1], AGES[5]),
    (TRAITS[3][2][1], TRAITS[3][2][4], AGES[5]),
    (TRAITS[3][2][3], TRAITS[7][2][1], AGES[5]),
    (TRAITS[5][0][1], TRAITS[5][0][2], AGES[5]),
    (TRAITS[5][2][0], TRAITS[5][2][1], AGES[5]),
    (TRAITS[5][2][1], TRAITS[8][1][2], AGES[5]),
    (TRAITS[5][2][2], TRAITS[5][1][2], AGES[5]),
    (TRAITS[6][0][0], TRAITS[6][0][1], AGES[5]),
    (TRAITS[6][0][1], TRAITS[6][0][0], AGES[5]),
    (TRAITS[6][0][2], TRAITS[9][0][2], AGES[5]),
    (TRAITS[6][2][1], TRAITS[6][2][0], AGES[5]),
    (TRAITS[6][2][2], TRAITS[6][2][3], AGES[5]),
    (TRAITS[7][2][0], TRAITS[7][2][4], AGES[5]),
    (TRAITS[7][2][1], TRAITS[7][2][0], AGES[5]),
    (TRAITS[7][2][2], TRAITS[7][2][3], AGES[5]),
    (TRAITS[8][1][0], TRAITS[8][1][2], AGES[5]),
    (TRAITS[8][2][0], TRAITS[8][2][1], AGES[5]),
    (TRAITS[3][1][1], TRAITS[3][1][0], AGES[6]),
    (TRAITS[3][2][1], TRAITS[3][2][3], AGES[6]),
    (TRAITS[3][2][4], TRAITS[3][2][2], AGES[6]),
    (TRAITS[7][0][0], TRAITS[7][0][1], AGES[6]),
    (TRAITS[8][1][0], TRAITS[8][1][1], AGES[6]),
    (TRAITS[8][1][2], TRAITS[8][1][0], AGES[6]),
    (TRAITS[8][2][0], TRAITS[8][2][2], AGES[6]),
    (TRAITS[8][2][1], TRAITS[8][2][3], AGES[6]),
    (TRAITS[8][2][2], TRAITS[8][2][1], AGES[6]),
    (TRAITS[8][2][3], TRAITS[8][2][0], AGES[6]),
    (TRAITS[9][0][0], TRAITS[9][0][1], AGES[6]),
    (TRAITS[9][0][1], TRAITS[9][0][2], AGES[6]),
    (TRAITS[9][0][2], TRAITS[9][0][0], AGES[6]),
]

TRAIT_SYNERGIES = [   
    (('curious', 'inquisitive'), 'enhances learning speed for knowledge-seeking skills'),
    (('cheerful', 'optimistic'), 'boosts creativity-related skill gains'),
    (('friendly', 'empathetic'), 'improves social relationships and diplomacy'),
    (('diligent', 'dedicated'), 'increases productivity and work efficiency'),
    (('creative', 'innovative'), 'enhances problem-solving and critical thinking'),
    (('shy', 'reserved'), 'reduces social anxiety and improves self-confidence'),
    (('moody', 'passionate'), 'increases emotional intensity and creativity'),
    (('anxious', 'sensitive'), 'improves emotional intelligence and empathy'),
    (('pessimistic', 'cynical'), 'increases critical thinking and skepticism'),
    (('conformist', 'traditional'), 'improves social standing and reputation'),
    (('rebellious', 'nonconformist'), 'increases independence and self-reliance'),
    (('insecure', 'self-doubting'), 'improves self-awareness and personal growth'),
    (('stubborn', 'unyielding'), 'increases determination and perseverance'),
    (('uncritical', 'naive'), 'improves open-mindedness and adaptability'),
    (('distracted', 'disorganized'), 'reduces procrastination and improves time management'),
    (('manipulative', 'deceptive'), 'increases persuasion and negotiation skills'),
    (('confrontational', 'aggressive'), 'increases assertiveness and conflict resolution skills'),
    (('workaholic', 'obsessive'), 'increases productivity and work efficiency'),
    (('indecisive', 'hesitant'), 'improves decision-making and risk-taking'),
    (('materialistic', 'greedy'), 'increases wealth and material possessions'),
    (('judgmental', 'critical'), 'increases critical thinking and discernment'),
    (('hedonistic', 'self-indulgent'), 'increases pleasure and enjoyment'),
    (('cynical', 'jaded'), 'increases skepticism and critical thinking'),
    (('regretful', 'remorseful'), 'improves self-awareness and personal growth'),
    (('bitter', 'resentful'), 'increases emotional intensity and motivation'),
    (('disengaged', 'detached'), 'reduces emotional attachment and increases independence'),
    (('controlling', 'manipulative'), 'increases persuasion and negotiation skills'),
    (('resentful', 'vindictive'), 'increases motivation and drive'),
    (('mentoring', 'guiding'), 'improves leadership and teaching skills'),
    (('philanthropic', 'altruistic'), 'increases generosity and kindness'),
    (('inspiring', 'visionary'), 'increases charisma and leadership skills'),
    (('reflective', 'introspective'), 'improves self-awareness and personal growth'),
    (('private', 'reserved'), 'reduces social anxiety and improves self-confidence'),
    (('traditional', 'conservative'), 'improves social standing and reputation'),
    (('adaptable', 'easy-going'), 'enhances flexibility and stress management'),
    (('engaging', 'sociable'), 'boosts charisma and social influence'),
    (('hopeful', 'joyful'), 'increases resilience and positivity'),
    (('self-aware', 'confident'), 'enhances personal growth and self-acceptance'),
    (('goal-oriented', 'ambitious'), 'increases focus and achievement'),
    (('generous', 'compassionate'), 'strengthens community bonds and support'),
    (('pragmatic', 'flexible'), 'improves problem-solving and adaptability'),
    (('mellow', 'balanced'), 'enhances emotional stability and calmness'),
    (('reflective', 'philosophical'), 'deepens understanding and wisdom'),
    (('authentic', 'principled'), 'promotes integrity and trustworthiness'),
]

for before, after, age in TRAIT_EVOLUTIONS:
    print("Your character's "+before+"trait evolved into "+after+"in the "+age+"stage og their life")