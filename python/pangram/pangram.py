def is_pangram(sentence):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    result = (all(i in sentence.lower() for i in alpha))
    print(result)

is_pangram('????Th fiv boxing wizards jump quickly')