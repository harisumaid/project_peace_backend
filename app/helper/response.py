import json
from flask import jsonify

def createResponse(success,message={},body={}):
    if(success):
        return jsonify(success,body)
    else:
        return jsonify(success,message)
