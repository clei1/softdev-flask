#import flask
from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
#if anyone goes slash to my website, "/" is the root of the website, run root()
def root():
    #bulk of code goes in here
    #print displays in console, shell, command line
    print 'PRINTING!!!!!!!!'
    #anything you return displays as html on website
    return "Hi everybody!"

@my_app.route('/foo')
#if anyone goes slash to my website, "/" is the root of the website, run root()
def foo():
    return "foo!"

@my_app.route('/anotherroute')
def anotherroute():
    return "anotherroute!"

if __name__ == '__main__':
    #automatically refreshes when you save
    my_app.debug = True;
    
    #if you were to import app.py, then don't run this
    #usual for this to exist, write test case even if you are importing
    my_app.run()
