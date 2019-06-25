def find_anagrams(word, candidates):
    
    chars = [char for char in word.lower()]
    # chars1 = ''.join(chars.sort(key=lambda x: x.lower()))
    chars = ''.join(sorted(chars))
    
    print(chars)
    print(candidates[0])
    sorted_candidates = []
    answer = []
    for x in candidates:
        sorted_candidates.append(''.join(sorted(x.lower())))
    print(sorted_candidates)
    for y in range(len(sorted_candidates)):
        if sorted_candidates[y] == chars and candidates[y] != word and candidates[y].lower() != word.lower():
            answer.append(candidates[y])
    print(answer)
    return(answer)
   
    

find_anagrams("BANANA", ["BANANA", "Banana", "banana"])