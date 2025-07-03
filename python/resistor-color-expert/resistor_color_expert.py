def resistor_label(colors):
    color_codes=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    tolerance_values = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
                    }
    if len(colors)==1:
        return '0 ohms'
    if len(colors)==4:
        value1=color_codes.index(colors[0]) * 10 + color_codes.index(colors[1])
        multiplier= 10 ** color_codes.index(colors[2])
        resistance=value1 * multiplier
        tolerance = tolerance_values[colors[-1]]
        if resistance >=1000:
            kiloohms = resistance / 1000
            if kiloohms.is_integer():
                return f"{int(kiloohms)} kiloohms {tolerance}"
            else:
                return f"{kiloohms:.1f} kiloohms {tolerance}"
        else:
            return str(resistance) + ' ohms ' + tolerance
    if len(colors) == 5:
        value1 = color_codes.index(colors[0]) * 100 + color_codes.index(colors[1]) * 10 + color_codes.index(colors[2])
        value2 = 10 ** color_codes.index(colors[3])
        resistance = value1 * value2
        tolerance = tolerance_values[colors[-1]]
        if resistance >= 1_000_000:
            megaohms = resistance / 1_000_000
            formatted = f"{megaohms:.2f}".rstrip('0').rstrip('.')
            return f"{formatted} megaohms {tolerance}"
        elif resistance >= 1000:
            kiloohms = resistance / 1000
            if kiloohms.is_integer():
                return f"{int(kiloohms)} kiloohms {tolerance}"
            else:
                return f"{kiloohms:.2f} kiloohms {tolerance}"
        else:
            return f"{resistance} ohms {tolerance}"

        
      


