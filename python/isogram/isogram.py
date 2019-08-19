import re

def is_isogram(string):
    string = string.lower()
    remove_chars = ' -'
    for i in remove_chars:
        string = string.replace(i, '')
    string_list = [char for char in string]
    
    return string_list


print(is_isogram("Emily-Jung Schwartzkopf"))