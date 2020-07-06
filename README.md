# Morse Code Translator

A web-based Morse Code Translater that converts english text and punctuation symbols into morse code and vice-versa with the letters being separated by a space, and words being separated by a '/'.

## Getting Started

Please make sure to do **all** of this before you run the code.

### Prerequisites

* Python 

* Flask

### Installing

##### Steps for installing Flask on Mac:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

Type all of this in the terminal

```
$ pip3 install virtualen
$ mkdir morseCodeTranslator
$ cd morseCodeTranslator
$ virtualenv venv --system-site-packages
$ source venv/bin/activate
(venv) $ pip3 install Flask
```
##### Steps for installing Flask on windows:

```
$ pip3 install virtualenv
$ mkdir morseCodeTranslator
$ cd morseCodeTranslator
$ py -3 -m venv venv
$ venv\Scripts\activate
(venv) $ pip3 install flask
```

## Running 

##### For running it on a Mac

Type all of this in the terminal

```
$ export FLASK_APP=app.py
$ flask run
```

##### For running it on Windows

```
$ flask run
````

Visit http://127.0.0.1:5000 to see the app running

## Usage

The usage is pretty straightforward and the step by step instructions are provided on the website

In morse code : The letters are separated by white-spaces and the words are separated by forward-slashes.

## Screenshots

### Homepage

![Morse1](https://user-images.githubusercontent.com/51927760/86534023-f3cec980-bef2-11ea-9eb2-0928bcbd618a.png)

### English to Morse

![Screenshot 2020-07-05 at 18 06 40](https://user-images.githubusercontent.com/51927760/86534130-7fe0f100-bef3-11ea-8936-77cdc67b3211.png)

### English to Morse Answer

![eng_to_morse_ans](https://user-images.githubusercontent.com/51927760/86534172-df3f0100-bef3-11ea-80ca-c1937fff5fe8.png)

### Morse to English Answer

![Morse_to_eng](https://user-images.githubusercontent.com/51927760/86534168-d51d0280-bef3-11ea-94ed-4e02625e5437.png)

## Built with

* [Python](https://www.python.org/) - Programming Language used

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The Web Framework used

* HTML - Markup Language used

* CSS - Style Sheet Language used

## Authors
* **Adithya Neelakantan**

* **Hrishikesh Mulkutkar**

* **Ayush Kapasi**
