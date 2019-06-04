import numpy as np

class Character:
    # def __init__(self):
    #     pass
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma, hitpoints):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hitpoints = hitpoints

    def dice(self):
        abilities = ['self.strength', 'self.dexterity', 'self.constitution', 'self.intelligence', 'self.wisdom', 'self.charisma']
        scores = []
        for x in range(len(abilities)):

        # abilities = {self.strength: 0, 'self.dexterity': 0, 'self.constitution': 0, 'self.intelligence': 0, 'self.wisdom': 0, 'self.charisma': 0}
            dice = np.random.randint(1,6,4)
            dice[::-1].sort()
            dice = np.delete(dice, -1)
            # print(dice)
            points = sum(dice)
            scores.append(points)
        # return points
        # abilities_new = {k: points for k, points in abilities.items()}
            
        print(abilities)
        print(scores)
        d = {k:v for k,v in zip(abilities,scores)}
        for k, v in d.items():
            print(k,v)

    
c1 = Character(0,0,0,0,0,0,0)

c1.dice()
