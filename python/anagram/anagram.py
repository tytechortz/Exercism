def find_anagrams(word, candidates):
    chars = [char for char in word]
    print(chars)
    print(''.join(sorted(chars)))
    

find_anagrams("master", ["stream", "maters"])