# coding: utf8 
import numpy as np
from flask import Flask
from flask import request
from flask_restful import Api, Resource, reqparse
import json
import bjoern
from numpy import dot
from numpy.linalg import norm
from flask_cors import CORS
import ast
import requests
import functions
PATH='/www/data/'
#app = falcon.API()
app = Flask(__name__)
CORS(app)

def cos_sim(a,b):
    cos_sim = dot(a, b)/(norm(a)*norm(b))
    return cos_sim

@app.route('/getInfos', methods=['GET', 'POST'])
def getInfos():
   j_data = request.json
   text = j_data['text']
   email = functions.extract_email(text)
   phone = functions.find_phone(text)
   return {"email":email, "phone":phone, "localisation":functions.location(phone)}

if __name__ == '__main__':
    bjoern.run(app, host='0.0.0.0',port = 80)
