import os
from flask import Flask, jsonify, make_response, render_template
from flask_restx import Api, Resource
from dotenv import load_dotenv
from poke_repository import get_berry_data
from poke_statistics import calculate_statistics, create_histogram

load_dotenv()

app = Flask(__name__)
api = Api(app, version='1.0', title='API Documentation',
          description='API endpoints for PokeAPI', doc='/docs')

POKEAPI_BASE_URL = os.getenv('POKEAPI_BASE_URL')


@api.route('/allBerryStats')
class AllBerryStats(Resource):
    def get(self):
        growth_times, berry_names = get_berry_data(POKEAPI_BASE_URL)

        if growth_times is None:
            response = jsonify({'error': 'Could not fetch data from PokeAPI'})
            response.status_code = 500
            return response

        stats = calculate_statistics(growth_times)
        create_histogram(growth_times)

        response_data = {
            "berries_names": berry_names,
            **stats
        }

        response = make_response(jsonify(response_data))
        response.headers['Content-Type'] = 'application/json'
        return response


@api.route('/histogram')
class Histogram(Resource):
    def get(self):
        return render_template('histogram.html')


if __name__ == '__main__':
    app.run(debug=True)
