import re

def is_isogram(string):
    string = string.lower()
    string = re.sub("\s", "", string)
    string_list = [char for char in string]
    
    return string_list


print(is_isogram("Emily Jung Schwartzkopf"))