import os
from xml.dom import ValidationErr
import pymongo
from flask import request
from app.validator.userValidation import userSignUpValidation
from app.helper.response import createResponse

MONGO_URI=os.getenv('MONGO_URI')
db = pymongo.MongoClient(MONGO_URI).get_default_database('project_peace')


def sign_up_controller():
    try:
        body = request.json
        email = body.get("email")
        password = body.get("password")
        req_body = dict([
            ('email',email),
            ('password',password)
        ])

        curr_validation = userSignUpValidation.validate(req_body)

        if(not curr_validation):
            print("validation failed")
            return createResponse(False,userSignUpValidation.errors),400
        else:
            if_present = db.users.find_one({'email':req_body['email']});
            # print(req_body)
            if if_present:
                # print(if_present)
                return createResponse(False,"User email already present"),409
            else :
                result = db.users.insert_one(req_body)
                # print(result.acknowledged)            
                return createResponse(True,{},req_body),200
        
    except ValidationErr as e:
        return e