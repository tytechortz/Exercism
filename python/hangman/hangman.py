# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

guesses = []
alpha = list('abcdefghijklmnopqrstuvwxyz')
word = list(input("Enter word: "))
letters = ''
for letter in word:
    letters += '_' 
print(letters)

# print(pre_answer)








# class Hangman(object):
#     def __init__(self, word):
#         self.remaining_guesses = 9
#         self.status = STATUS_ONGOING
        
        
#     def guess(self, char):
#         guesses.insert(0,char)
#         if char in word:
#             print('correct')
#             self.remaining_guesses -= 1
#         else:
#             print('incorrect')
#             self.remaining_guesses -= 1
#         print("You have guessed {}:".format(guesses))
#         print("You have {} guesses left".format(self.remaining_guesses))
       

#     def get_masked_word(self):
#         pass

#     def get_status(self):
#         pass

# def play():
#     a = Hangman(word)
#     a.guess(input("Enter letter: "))

# play()






       