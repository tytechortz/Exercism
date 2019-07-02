def find_anagrams(word, candidates):
    
    chars = [char for char in word.lower()]
    chars = ''.join(sorted(chars))
    
    sorted_candidates = []
    answer = []
    for x in candidates:
        sorted_candidates.append(''.join(sorted(x.lower())))
   
    for y in range(len(sorted_candidates)):
        if sorted_candidates[y] == chars and candidates[y] != word and candidates[y].lower() != word.lower():
            answer.append(candidates[y])
    return answer
   
