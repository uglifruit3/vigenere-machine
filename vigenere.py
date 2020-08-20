# this program performs basic operations involving the vigenere cipher

# for clearing screen
import os

#**************************
# FUNCTION DEFINITIONS
#**************************

# displays the homescreen upon program invocation
def homescreen():
    os.system("cls") # clear screen - IF USING UNIX-LIKE OS, CHANGE TO "clear"
    print("""
 __ __  ____   ____    ___  ____     ___  ____     ___      ___ ___   ____    __  __ __  ____  ____     ___ 
|  |  ||    | /    |  /  _]|    \   /  _]|    \   /  _]    |   |   | /    |  /  ]|  |  ||    ||    \   /  _]   
|  |  | |  | |   __| /  [_ |  _  | /  [_ |  D  ) /  [_     | _   _ ||  o  | /  / |  |  | |  | |  _  | /  [_ 
|  |  | |  | |  |  ||    _]|  |  ||    _]|    / |    _]    |  \_/  ||     |/  /  |  _  | |  | |  |  ||    _]
|  :  | |  | |  |_ ||   [_ |  |  ||   [_ |    \ |   [_     |   |   ||  _  /   \_ |  |  | |  | |  |  ||   [_ 
 \   /  |  | |     ||     ||  |  ||     ||  .  \|     |    |   |   ||  |  \     ||  |  | |  | |  |  ||     |
  \_/  |____||___,_||_____||__|__||_____||__|\_||_____|    |___|___||__|__|\____||__|__||____||__|__||_____|

    Please select an option:
    [1] Encrypt
    [2] Decrypt""")

# displays the standard options screen once an operation has been completed
def choiceScreen():
    print("\n" + """==========COMPLETED==========
    Please select an option:
    [1] Encrypt
    [2] Decrypt
    [3] Export to .txt file
    [4] Quit""")

# gets user input from the homescreen
def optionChoice():
    choice = input()
    valid = ["1", "2"]
    while choice not in valid:
        # sanitizing user input
        print("Invalid entry")
        choice = input()
    return int(choice)

# gets user input when further options are available
def furtherOptions():
    choice = input()
    valid = ["1", "2", "3", "4"]
    while choice not in valid:
        # sanitizing user input
        print("Invalid entry")
        choice = input()
    return int(choice)
   
# gets user input for a string and converts into a list of ascii characters
def getInput():
    wordsIn = input()
    wordsIn = wordsIn.upper()
    listForm = []
    for i in range(len(wordsIn)):
        listForm.append(wordsIn[i])
    return listForm

# performs vigenere encryption, including getting user inputs
def encrypt():
    os.system("cls")
    print("Please enter the plaintext")
    plaintext = getInput()
    print("Please enter encryption key")
    key = getInput()
    
    # building a string of the given key that is of equivalent length to the plaintext
    newKey = []
    for i in range(len(plaintext)):
        a = divmod(i, len(key))
        b = i - (len(key) * a[0])
        newKey.append(key[b])

    output = []
    for i in range(len(plaintext)):
        if ord(plaintext[i]) <= 64:
            # if the character is not a letter, do not alter it
            newChar = ord(plaintext[i])
        elif ord(plaintext[i]) > 64:
            newChar = 65 + (ord(plaintext[i]) - 65) + (ord(newKey[i]) - 65)
            if newChar > 90:
                newChar = newChar - 26
        output.append(chr(newChar))

    final = "".join(output)
    return final

# performs vigenere decryptions, including getting user inputs
def decrypt():
    os.system("cls")
    print("Please enter the encrypted text")
    encrypted = getInput()
    print("Please enter the encryption key")
    key = getInput() 

    # building equal-length key string
    newKey = []
    for i in range(len(encrypted)):
        a = divmod(i, len(key))
        b = i - (len(key) * a[0])
        newKey.append(key[b])

    output = []
    for i in range(len(encrypted)):
        if ord(encrypted[i]) <= 64:
            newChar = ord(encrypted[i])
        elif ord(encrypted[i]) > 64: 
            newChar = ord(encrypted[i]) - ord(newKey[i]) + 65
            if newChar < 65:
                newChar = newChar + 26
        output.append(chr(newChar))

    final = "".join(output)
    return final
    
# exports text to a .txt file of the user's choosing
def txtExport(text):
    os.system("cls")
    title = input("File name: ")
    path = input("Path (delineate with forward slashes (/)) (press [%] for current path): ")
    if path == "%":
        newFile = open(title + ".txt", "w") # building ostream object for file in question
    else:
        newFile = open(path + title + ".txt", "w") # same, but with specified path

    newFile.write(text)
    newFile.close()
    print("Export complete")


#**************************
# MAIN PROGRAM
#**************************

homescreen() # print homescreen
selection = optionChoice() # getting initial user selection
while True:
    if selection == 1: # encrypt
        text = encrypt()
        print("\n" + "ENCRYPTED TEXT:  " + text)
        choiceScreen()
        selection = furtherOptions()
    elif selection == 2: # decrypt
        text = decrypt()
        print("\n" + "DECRYPTED TEXT:  " + text)
        choiceScreen()
        selection = furtherOptions()
    elif selection == 3: # export to txt
        txtExport(text)
        choiceScreen()
        selection = furtherOptions()
    elif selection == 4: # quit
        break
