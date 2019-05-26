def reverse(text):
    chars = list(text)
    reversed_text = []
    for i in chars:
        reversed_text.insert(0,i)
    return("".join(reversed_text))
    
reverse('hello')
