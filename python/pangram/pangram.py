def is_pangram(sentence):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    result = (all(i in sentence.lower() for i in alpha))
    print(result)

