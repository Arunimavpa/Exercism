def commands(binary_str):
    actions=["wink","double blink","close your eyes","jump"]
    bit=list(binary_str)
    result=[]
    bit.reverse()

    for i in range(4):
        if bit[i] == '1':
            result.append(actions[i])

    if len(bit)>4 and bit[4] == '1':
        result.reverse()
    return result