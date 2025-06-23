def is_isogram(string):
    letters=[char.lower() for char in string if char.isalpha()]
    for char in letters:
            if letters.count(char) > 1:
                return False
    return True
