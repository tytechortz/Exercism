import numpy

class Character:
    def __init__(self):
        pass
    def rand_gen(self):
        dice = numpy.random.randint(1,6,4)

        # for i in range(4):
        #     rand_list = numpy.random.randint(1,6,4)
        #     dice.append(rand_list)

        print(dice)

c1 = Character()

c1.rand_gen()
