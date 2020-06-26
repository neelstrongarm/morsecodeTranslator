<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>
            Morse Code Translator
        </title>
        <style>
            .heading
            {
                color : rgb(179, 42, 83);
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; 
                text-align: center; 
                /* padding-top: 50px; */
                font-size: 1in; 
                
            }
            .division1
            {
                float:left;
                text-align: center;
                padding: 100px;
                background-color: rgb(32, 204, 204);
            }
            .division2
            {
                float:right;
                text-align: center;
                padding: 100px;
                background-color: rgb(32, 204, 204);
            }

            .butt
            {
                padding-left:  100px;
                padding-right: 100px;
                padding-top: 20px;
                padding-bottom: 20px;
                border: solid black;
                background-color: rgb(18, 80, 131); 
                color: white;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; 
                font-size: large;
            }
            .para
            {
                text-align: center;
                font:bolder;
                color: rgb(33, 46, 45);
                font-family: Georgia;
            }
        </style>

    </head>

    <body style='background-color: rgb(32, 204, 204)'>
       <h1 class=heading >Morse Code Translator</h1>
        <p class=para>
            Morse code is a method used in telecommunication to encode <br>text characters as standardized sequences<br> of two different signal durations, <br>called dots and dashes or dits and dahs.
        </p>
        <div class=division1>
            <form action="/eng_to_morse_butt">
                <button type="submit" class=butt method="GET">ENGLISH TO MORSE</button>
            </form>
        </div>
        <div class=division2>
            <form action="/morse_to_eng_butt">
                <button type="submit" class=butt method="GET">MORSE TO ENGLISH</button>
            </form>
        </div>
    </body>
</html>
