from collections import Counter

dice = []
# Score categories
# Change the values as you see fit
YACHT = 50
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: dice.count(2)
THREES = lambda dice: dice.count(3)
FOURS = lambda dice: dice.count(4)
FIVES = lambda dice: dice.count(5)
SIXES = lambda dice: dice.count(6)
FULL_HOUSE = lambda dice: if len(set(dice)) == 2:sort_dice = sorted(dice)
            if sort_dice[-1] == sort_dice[-2] and sort_dice[0] == sort_dice[1]:
                return(sum(dice))
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    return category(dice) 
    # print(category)
    # if category == YACHT:
    #     if len(set(dice)) == 1:
    #         return YACHT
    # elif category == ONES:
    #     # print(dice.count(1))
    #     return ONES
    # elif category == TWOS:
    #     # return(2 * dice.count(2))
    #     return TWOS
    # elif category == 'THREES':
    #     return(3 * dice.count(3))
    # elif category == 'FOURS':
    #     return(4 * dice.count(4))
    # elif category == 'FIVES':
    #     return(5 * dice.count(5))
    # elif category == 'SIXES':
    #     return(6 * dice.count(6))
    # elif category == 'FULL_HOUSE':
    #     if len(set(dice)) == 2:
    #         sort_dice = sorted(dice)
    #         if sort_dice[-1] == sort_dice[-2] and sort_dice[0] == sort_dice[1]:
    #             return(sum(dice))
    # elif category == 'FOUR_OF_A_KIND':
    #     sort_dice = sorted(dice)
    #     if sort_dice[-1] == sort_dice[-4]:
    #         return(sum(sort_dice[1:5]))
    #     elif sort_dice[0] == sort_dice[3]:
    #         return(sum(sort_dice[:4]))  
    # elif category == 'LITTLE_STRAIGHT':
    #     sort_dice = sorted(dice)
    #     if len(set(dice)) >= 4:
    #         if sort_dice[0] == sort_dice[3] - 3 or sort_dice[1] == sort_dice[4] - 3 or sort_dice[4] == (sort_dice[0] + 4):
    #             return(30)
    # elif category == 'BIG_STRAIGHT':
    #     sort_dice = sorted(dice)
    #     if sort_dice[4] == (sort_dice[0] + 4):
    #         return(40)
    # elif category == 'CHOICE':
    #     return(sum(dice))




# score([2, 3, 4, 5, 6], TWOS)
