def label(colors):
    color_codes=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    color1=color_codes.index(colors[0])
    color2=color_codes.index(colors[1])
    color3=color_codes.index(colors[2])
    index_12=color1 * 10 + color2
    index_3= 10 ** color3
    resistance=index_12 * index_3
    if resistance >= 1000000000 :
        return str(resistance//1000000000) + ' gigaohms'
    elif resistance >= 1000000 :
        return str(resistance//1000000) + ' megaohms'
    elif resistance >= 1000:
        return str(resistance//1000)  + ' kiloohms'
    else:
        return str(resistance) + ' ohms'
