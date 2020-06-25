# Morse Code Translater

# A dictionary which maps letters to morse code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                        'C':'-.-.', 'D':'-..', 'E':'.', 
                        'F':'..-.', 'G':'--.', 'H':'....', 
                        'I':'..', 'J':'.---', 'K':'-.-', 
                        'L':'.-..', 'M':'--', 'N':'-.', 
                        'O':'---', 'P':'.--.', 'Q':'--.-', 
                        'R':'.-.', 'S':'...', 'T':'-', 
                        'U':'..-', 'V':'...-', 'W':'.--', 
                        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                        '1':'.----', '2':'..---', '3':'...--', 
                        '4':'....-', '5':'.....', '6':'-....', 
                        '7':'--...', '8':'---..', '9':'----.', 
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                        '?':'..--..', '/':'-..-.', '-':'-....-', 
                        '(':'-.--.', ')':'-.--.-', "'" : '.----.',
                        '&':'.-...','@':'.--.-.',':':'---...',
                        '!':'-.-.--','+':'.-.-.','=':'-...-', ',' : '--..--'} 

# Function to convert English letters to Morse
def englishToMorse(s): 
    # Separating letter with spaces and words with forward slash
    ans = []
    for i in s:
        if i == " ":
            ans.append('/')
        elif i.upper() not in MORSE_CODE_DICT:
            return -1
        else:
            ans.append(MORSE_CODE_DICT[i.upper()])
    letters = ' '.join(ans)
    return letters


# Function to convert Morse to English
def morseToEnglish(s):
    # Creating a new dictionary, which maps morse code to letters
    eng_dict = {} 
    for i in MORSE_CODE_DICT:
        eng_dict[MORSE_CODE_DICT[i]] = i.lower()
    # Separating letter with spaces and words with forward slash
    words = s.split('/') 
    ans = []
    for i in words:
        letter = i.split()
        for j in letter:
            ans.append(eng_dict[j])
        ans.append(' ')
    fin = ''.join(ans)
    # Design Decision here
    return fin.capitalize()
    

# Error Handling for the choice
while True:
    try:
        choice = int(input("1 for Morse to English\n2 for English to Morse\nEnter choice: "))
        if choice == 1 or choice == 2:
            break
        else:
            print('Error!!')
    except ValueError:
        print("Oops, you must enter either 1 or 2")


# Driver for Morse to English
if choice == 1:
    x = None
    while True:
        s = input("Please enter Morse Code: ").rstrip()
        x = morseToEnglish(s)
        if x != -1:
            break
        else:
            print("Error!!!")
    print(f"The Morse Code in English is : {x}" )

# Driver for English to Morse
if choice == 2:
    x = None
    while True:
        s = input("Please enter the String: ").rstrip()
        x = englishToMorse(s)
        if x != -1:
            break
        else:
            print("Error!!!")
    print(f"The Morse Code is : {x.strip()}" )
