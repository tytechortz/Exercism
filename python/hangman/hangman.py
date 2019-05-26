# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

guesses = []


word = list(input("Enter word: "))
print(word)


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        

    def guess(self, char):
        
        guesses.insert(0,char)
        self.remaining_guesses -= 1
        
        print(guesses)

    def get_masked_word(self):
        pass

    def get_status(self):
        
        print(word)



# a = Hangman(word)
# a.guess(input("Guess letter: "))
       