# Morse Code Translator

A web-based Morse Code Translater

## Getting Started

Please make sure to do all of this before you run the code.

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

### Folders
##### In the directory "morseCodeTranslator"
* Create a new folder and name it "templates"

  Copy all of the ".html" extention files to "templates" folder.
 
* Create a new folder and name it "static"

  Copy the image "dog.jpg" in the "static" folder.

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

The usage is pretty straightforward and the step by step instructions and provided on the website

In morse code : The letters are separated by white-spaces and the words are separated by forward-slashes.

## Built with

* [Python](https://www.python.org/) - Programming Language used

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The Web Framework used

* HTML - Markup Language used

* CSS - Style Sheet Language used


## Authors
* **Adithya Neelakantan**

* **Hrishikesh Mulkutkar**

* **Ayush Kapasi**
