from flask import jsonify


class CustomException(Exception):
    status_code = 500
    message = "Internal Server Error"

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def handle_custom_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
