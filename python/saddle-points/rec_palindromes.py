def isPalindrome(word):
    if len(word) <= 1:
        return True

    if word[0] != word[len(word) - 1]:
        return False

    
    return isPalindrome(word[1:-1])

print(isPalindrome('noon'))