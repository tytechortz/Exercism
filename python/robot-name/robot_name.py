import random
import string

class Robot(object):
    def __init__(self):
        pass

    def getLetters(self,size=2, chars=string.ascii_uppercase):
        print(''.join(random.choice(chars) for _ in range(size)))

    def getNumbers(self,size=3, chars=string.digits):
        print(''.join(random.choice(chars) for _ in range(size)))


r = Robot()
r.getLetters()
r.getNumbers()