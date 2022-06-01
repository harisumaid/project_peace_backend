from crypt import methods
from flask import Blueprint,request
from .controller import sign_up

main = Blueprint('main',__name__)

@main.route("/")
def main_route():
    return "BluePrint route test"

@main.route("/sign-up", methods=["POST"])
def sign_up_route():    
    # email = request.json.email
    # password = request.json.password
    return sign_up.sign_up_controller()
