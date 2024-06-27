import os
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from routes.poke_routes import api as poke_namespace
from exceptions import handle_custom_exception, CustomException
from extensions import cache

load_dotenv()

app = Flask(__name__)

app.config['POKEAPI_BASE_URL'] = os.getenv('POKEAPI_BASE_URL')
app.config['CACHE_TYPE'] = 'SimpleCache' 
app.config['CACHE_DEFAULT_TIMEOUT'] = 300 

cache.init_app(app)

api = Api(app, version='1.0', title='API Documentation',
          description='API endpoints for PokeAPI', doc='/docs')


api.add_namespace(poke_namespace)

app.register_error_handler(CustomException, handle_custom_exception)
