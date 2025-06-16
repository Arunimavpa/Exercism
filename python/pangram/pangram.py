def is_pangram(sentence):
    sentence=sentence.lower()
    alphabet='abcdefghijklmnopqrstuvswxyz'
    for char in alphabet:
        if char not in sentence:
            return False
    return True
