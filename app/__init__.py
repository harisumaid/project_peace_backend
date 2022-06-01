from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from .views import main
from .helper.my_encoder import MyEncoder

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app,resources={r"/*": {"origins": "*"}})
    app.json_encoder = MyEncoder
    app.register_blueprint(main)
    return app