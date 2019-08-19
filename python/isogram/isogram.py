def is_isogram(string):
    string = string.lower()
    string_list = [char for char in string]
    
    return string_list


print(is_isogram("Isogram"))