def find_anagrams(word, candidates):
    chars = [char for char in word]
    chars = ''.join(sorted(chars))
    print(chars)
    print(candidates)
    sorted_candidates = []
    answer = []
    for x in candidates:
        sorted_candidates.append(''.join(sorted(x)))
    print(sorted_candidates)
    for y in range(len(sorted_candidates)):
        if sorted_candidates[y] == chars:
            answer.append(candidates[y])
    print(answer)
    

find_anagrams("master", ["stream", "maters", "bluff"])