# Morse Code Translater

from flask import Flask, render_template, request

# Initializong flask
app = Flask(__name__)


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


# Function for index.html
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    
# Function for eng_to_morse.html
@app.route('/eng_to_morse_butt')
def eng_to_morse():
        return render_template('eng_to_morse.html')

# Function for morse_to_eng.html
@app.route('/morse_to_eng_butt')
def morse_to_eng():
    return render_template('morse_to_eng.html')

# Function which converts morse to English
@app.route('/convert_morse_to_eng', methods=["GET", "POST"])
def morseToEnglish():
    if request.method == "POST":

        # Input from the user
        s = request.form.get("morse_code")
        # If the given input is empty, we render the apology page
        if len(s) ==0:
            message = "Input Field Empty"
            return render_template("apology.html", inp = message)

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
                # If an unrecognized character is given as input by the user, we render the apology page
                if j not in eng_dict:
                    message = "Unrecognised Character"
                    return render_template("apology.html", inp = message)

                ans.append(eng_dict[j])
    
            ans.append(' ')
        fin = ''.join(ans)
        return render_template("morse_to_eng_ans.html", ans = fin.title(), inp=s)


# Function that converts English to Morse
@app.route('/convert_eng_to_morse', methods=["GET", "POST"])
def convert_eng_to_morse():
    if request.method == "POST":

        # Input from the user
        s = request.form.get("given_input")
        # If the given input is empty, we render the apology page
        if len(s) ==0:
            message = "Input Field Empty"
            return render_template("apology.html", inp = message)

        ans = []
        for i in s:

            if i == " ":
                ans.append('/')
                
            # If an unrecognized character is given as input by the user, we render the apology page
            elif i.upper() not in MORSE_CODE_DICT:
                message = "Unrecognised Character"
                return render_template("apology.html", inp = message)

            else:
                ans.append(MORSE_CODE_DICT[i.upper()])

        letters = ' '.join(ans)
        return render_template("eng_to_morse_ans.html", ans = letters, inp = s)
