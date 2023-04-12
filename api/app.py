from flask import Flask,request
from logzero import logger
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing():
    return "Have a nice day! (1)", 200

@app.route('/lb-poke', methods=['GET'])
def lbPoke():
    return "The second make you wonder", 200
