usage = 1
while usage != "q":
    usage = input("Would you like to encode or decode? You can press 'Q' to quit at any time.\n")
    usage = usage.lower()
    if usage == "encode":
        message = input("Enter a message to encode:\n")
        message = message.upper()
        key = eval(input("What key would you like to encode this with (1-26)?\n"))
        output = ""
        for letter in message:
            if letter.isupper():
                value = ord(letter) + key
                letter = chr(value)
                if not letter.isupper():
                    value -= 26
                    letter = chr(value)
            output += letter
        print("Output message: ", output)
    elif usage == "decode":
        message = input("Enter a message to decode:\n")
        message = message.upper()
        key = eval(input("What key would you like to decode this with (1-26)?\n"))
        output = ""
        for letter in message:
            if letter.isupper():
                value = ord(letter) - key
                letter = chr(value)
                if not letter.isupper():
                    value += 26
                    letter = chr(value)
            output += letter
        print("Output message: ", output)
    elif usage == "q":
        print("Thanks for using my script! - Ryan")
        quit()
    elif input != "encode" and input != "decode":
        print("Invalid response.")
