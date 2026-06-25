FIRST_CHAR_CODE=ord("A")
LAST_CHAR_CODE=ord("Z")
CHAR_RANGE=26 

def ceaser_shift(message,shift):

    #result place holder
    result="" #empty string

    #go through each letter in the message by looping

    for char in message.upper():
        if char.isalpha():    #check if char is part of alphabet
            #convert character to ascii code
            char_code= ord(char)  #built in func to convert to code
            new_code = char_code + shift

            if new_code > LAST_CHAR_CODE:
                new_code -= CHAR_RANGE

            if new_code < FIRST_CHAR_CODE:
                new_code += CHAR_RANGE
    

            new_char= chr(new_code)
            # append the result to the result string
            result += new_char
            #print(f"{char} -> {char_code} -> {new_code} -> {new_char}")
        # to preserve unique characters

        else:
            result += char

    print("\n")
    print(message)
    print(result.lower())

user_message = input("Message to encrypt: ")
user_shift = int(input("Shift key (integer): "))
ceaser_shift(user_message,user_shift)
    