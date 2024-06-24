import os
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from routes.poke_routes import api as poke_namespace
from exceptions import handle_custom_exception, CustomException

load_dotenv()

app = Flask(__name__)
api = Api(app, version='1.0', title='API Documentation',
          description='API endpoints for PokeAPI', doc='/docs')

app.config['POKEAPI_BASE_URL'] = os.getenv('POKEAPI_BASE_URL')

api.add_namespace(poke_namespace)

app.register_error_handler(CustomException, handle_custom_exception)

if __name__ == '__main__':
    app.run(debug=True)
