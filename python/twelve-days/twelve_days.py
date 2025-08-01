def recite(start_verse, end_verse):
    ordinals = ("first", "second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth")

    gifts = (
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming",
    )
    
    verses=[]
    for day in range(start_verse , end_verse +1):
        verse =f"On the {ordinals[day-1]} day of Christmas my true love gave to me: "
        lines=[]
        for i in range(day-1,-1,-1):
            if i==0 and day > 1:
                lines.append( "and " +gifts[i])
            else:
                lines.append(gifts[i])
        full_verses=verse +", ".join(lines)+ "."
        verses.append(full_verses)
    return verses
