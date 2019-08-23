def is_isogram(string):
    string = string.lower()
    remove_chars = ' -'
    for i in remove_chars:
        string = string.replace(i, '')
    string_list = [char for char in string]

    if len(set(string_list)) == len(string):
        return True
    else:
        return False


