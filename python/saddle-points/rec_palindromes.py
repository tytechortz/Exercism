def is_palindrome(word):
    if len(word) <= 1:
        return True

    elif word[0] != word[len(word) - 1]:
        return False

    else:
        print(word)
        return is_palindrome(word[1:-1])

print(is_palindrome('abcdefgfedcba'))