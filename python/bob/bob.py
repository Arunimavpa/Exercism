def response(hey_bob):
    hey_bob = hey_bob.strip()
    if  not hey_bob:
        return 'Fine. Be that way!'  
    elif  hey_bob.endswith('?') and hey_bob.isupper():
        return "Calm down, I know what I'm doing!" 
    elif hey_bob.endswith('?'):
        return 'Sure.'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'                 
    else:
        return "Whatever."