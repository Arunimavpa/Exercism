def translate(text):
    vowel='aeiou'
    index=0
    if text[0] in vowel or text.startswith("xr") or text.startswith("yt"):
        return text + 'ay'
    
    if 'qu' in text:
        index= text.find('qu')+2
        return (text[index:] + text[:index] + 'ay')
    if 'y' in text and text.find('y')!=0:
        index = text.find('y')
        return (text[index:] + text[:index] + 'ay')

    for char in text :
        if char in vowel:
            break
        index += 1
    return (text[index:] + text[:index] + 'ay')



