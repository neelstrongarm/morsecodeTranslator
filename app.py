from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    
@app.route('/eng_to_morse_butt')
def eng_to_morse():
        return render_template('eng_to_morse.html')


@app.route('/morse_to_eng_butt')
def morse_to_eng():
    return render_template('morse_to_eng.html')

@app.route('/convert_morse_to_eng', methods=["GET", "POST"])
def morseToEnglish():
    # Creating a new dictionary, which maps morse code to letters
    if request.method == "POST":
        s = request.form.get("morse_code")
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
        return render_template("morse_to_eng_ans.html", ans = fin.title())
    
@app.route('/convert_eng_to_morse', methods=["GET", "POST"])
def convert_eng_to_morse():
    if request.method == "POST":
        s = request.form.get("given_input")
        ans = []
        for i in s:
            if i == " ":
                ans.append('/')
            elif i.upper() not in MORSE_CODE_DICT:
                return -1
            else:
                ans.append(MORSE_CODE_DICT[i.upper()])
        letters = ' '.join(ans)
        return render_template("eng_to_morse_ans.html", ans = letters)
