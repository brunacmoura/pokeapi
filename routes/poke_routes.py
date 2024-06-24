from flask import jsonify, make_response, render_template
from flask_restx import Namespace, Resource
from poke_repository import get_berry_data
from poke_statistics import calculate_statistics, create_histogram
from exceptions import CustomException

api = Namespace('berry', description='Berry related operations')

@api.route('/allBerryStats')
class AllBerryStats(Resource):
    def get(self):
        try:
            growth_times, berry_names = get_berry_data()
            if growth_times is None:
                raise CustomException("Could not fetch data from PokeAPI", status_code=500)

            stats = calculate_statistics(growth_times)
            create_histogram(growth_times)

            response_data = {
                "berries_names": berry_names,
                **stats
            }

            response = make_response(jsonify(response_data))
            response.headers['Content-Type'] = 'application/json'
            return response

        except CustomException as e:
            raise e

        except Exception as e:
            raise CustomException(f"An unexpected error occurred: {str(e)}", status_code=500)


@api.route('/histogram')
class Histogram(Resource):
    def get(self):
        try:
            return render_template('histogram.html')
        except Exception as e:
            raise CustomException(f"An unexpected error occurred: {str(e)}", status_code=500)
