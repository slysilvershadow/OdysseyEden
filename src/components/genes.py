from ..utils import constants as con
import random


class DNA:
    def __init__(self, gender=None, skin=None, height=None, body=None, hair=None, eyes=None, nose=None, mouth=None, ears=None):
        self.gender = gender or {
            'sex1': con.SEX[0],
            'sex2': random.choice(con.SEX),
            'gender1': random.choice(con.GENDER),
            'gender2': random.choice(con.GENDER)
        }
        self.skin = skin or {
            'tone1': random.choice(con.TONE),
            'tone2': random.choice(con.TONE),
            'undertone1': random.choice(con.UNDERTONE),
            'undertone2': random.choice(con.UNDERTONE)
        }
        self.height = height or {
            'value1': random.uniform(0.8, 1.2),
            'value2': random.uniform(0.8, 1.2),
            'proportion1': random.choice(con.HEIGHT),
            'proportion2': random.choice(con.HEIGHT)
        }
        self.body = body or {
            'shape1': random.choice(con.BSHAPE),
            'shape2': random.choice(con.BSHAPE),
            'size1': random.choice(con.BSIZE),
            'size2': random.choice(con.BSIZE)
        }
        self.hair = hair or {
            'color1': random.choice(con.HCOLOR),
            'color2': random.choice(con.HCOLOR),
            'texture1': random.choice(con.HTEXT),
            'texture2': random.choice(con.HTEXT)
        }
        self.eyes = eyes or {
            'shape1': random.choice(con.ESHAPE),
            'shape2': random.choice(con.ESHAPE),
            'color1': random.choice(con.ECOLOR),
            'color2': random.choice(con.ECOLOR)
        }
        self.nose = nose or {
            'profile1': random.choice(con.NPROFILE),
            'profile2': random.choice(con.NPROFILE),
            'shape1': random.choice(con.NSHAPE),
            'shape2': random.choice(con.NSHAPE)
        }
        self.mouth = mouth or {
            'shape1': random.choice(con.MSHAPE),
            'shape2': random.choice(con.MSHAPE)
        }
        self.ears = ears or {
            'shape1': random.choice(con.RSHAPE),
            'shape2': random.choice(con.RSHAPE),
            'size1': random.choice(con.RSIZE),
            'size2': random.choice(con.RSIZE)
        }

    def __repr__(self):
        return (f"DNA(gender={self.gender}, skin={self.skin}, height={self.height}, "
                f"body={self.body}, hair={self.hair}, eyes={self.eyes}, nose={self.nose}, "
                f"mouth={self.mouth}, ears={self.ears})")

    def __add__(self, other):
        if not isinstance(other, DNA):
            raise TypeError("Cannot combine DNA with non-DNA")

        def combine_attributes(attr1, attr2):
            return {
                key: random.choice([attr1[key], attr2[key]])
                for key in attr1.keys()
            }

        new_DNA = DNA(
            gender=combine_attributes(self.gender, other.gender),
            skin=combine_attributes(self.skin, other.skin),
            height=combine_attributes(self.height, other.height),
            body=combine_attributes(self.body, other.body),
            hair=combine_attributes(self.hair, other.hair),
            eyes=combine_attributes(self.eyes, other.eyes),
            nose=combine_attributes(self.nose, other.nose),
            mouth=combine_attributes(self.mouth, other.mouth),
            ears=combine_attributes(self.ears, other.ears)
        )

        return new_DNA
