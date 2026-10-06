from morse_dict import morse_dict

word = ""
c_type = "M"
letter_dict = {value: key for key, value in morse_dict.items()}

print("Type word or morse code to convert '!' to exit:\n")
while word != "!":
    word = input("Word: ").upper()
    for letter in word:
        if letter != "." and letter != "-" and letter != " " and letter != "/":
            c_type = "W"
    if c_type == "W":
        conversion_list = [morse_dict[letter] for letter in word]
        new_word = " ".join(conversion_list)
    else:
        morse_list = word.split()
        print(morse_list)
        conversion_list = [letter_dict[item] for item in morse_list]
        new_word = "".join(conversion_list)
    print(new_word)
    c_type = "M"






