import random
import string

class Robot(object):
    def __init__(self):
        self.letters = ''
        self.numbers = ''
        self.name = ''

    def getLetters(self,size=2, chars=string.ascii_uppercase):
        return self.letters.join(random.choice(chars) for _ in range(size))
        

    def getNumbers(self,size=3, chars=string.digits):
        return self.numbers.join(random.choice(chars) for _ in range(size))

    def getName(self):
        # print(r.getLetters() + r.getNumbers())
        self.name = r.getLetters() + r.getNumbers()
    

   
# r = Robot()
# print(r.getLetters() + r.getNumbers())
# print(r.name)


