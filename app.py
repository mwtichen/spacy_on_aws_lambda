# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 09:39:07 2021

@author: mwtichen
"""

from flask import Flask, request
import spacy
import json



app = Flask(__name__)

@app.route('/ner', methods = ['GET', 'POST'])
def get_ents():
    nlp = spacy.load('ner_model')
    
    text = request.args.get('sentence')
    
    
    doc = nlp(text)
    
    result = [(ent.text, ent.label_) for ent in doc.ents]
    
    response = {
        "statusCode": 200,
        "body": json.dumps(result)}
    
    return response

if __name__ == "__main__":
    app.run()
