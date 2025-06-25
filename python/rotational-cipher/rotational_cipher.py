def rotate(text, key):
    result= ""
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in text:
        if char.islower():
            index=lower.index(char)
            rotated=lower[(index + key)%26]
            result +=rotated
        elif char.isupper():
            index=upper.index(char)
            rotated=upper[(index + key)%26]
            result +=rotated
        else:
            result +=char

    return result
