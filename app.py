import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from poke_repository import get_berry_data
from poke_statistics import calculate_statistics

load_dotenv()

app = Flask(__name__)

POKEAPI_BASE_URL = os.getenv('POKEAPI_BASE_URL')


@app.route('/allBerryStats', methods=['GET'])
def all_berry_stats():
    growth_times, berry_names = get_berry_data(POKEAPI_BASE_URL)

    if growth_times is None:
        return jsonify({'error': 'Could not fetch data from PokeAPI'}), 500

    stats = calculate_statistics(growth_times)

    response = {
        "berries_names": berry_names,
        **stats
    }

    return jsonify(response), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)