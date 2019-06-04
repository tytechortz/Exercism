import numpy as np

class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        

    def ability(self):
        dice = np.random.randint(1,6,4)
        dice[::-1].sort()
        dice = np.delete(dice, -1)
        points = sum(dice)
        return points
        
def modifier(baseValue):
    return round(((baseValue - 10) // 2)-.1)
    
c1 = Character()

c1.ability()
