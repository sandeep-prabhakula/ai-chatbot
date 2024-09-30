import json
from flask import Flask, jsonify, request, make_response
from functions_framework import http
from utils import getOpenAiResponse
app2 = Flask(__name__)


@app2.after_request
def remove_server_header(response):

    response.headers.pop("Server", None)

    response.headers.pop("X-Powered-By", None)
    return response


@app2.route("/", methods=['POST', "OPTIONS"])
def process():

    try:
        if request.method == "OPTIONS":
            return _build_cors_preflight_response()
        elif request.method != "POST":
            return jsonify({"error": "INVALID_REQUEST_BODY"}), 405
        else:
            data = request.get_json()
            response = getOpenAiResponse(data['prompt'])

            status = response.get("statusCode")

            if status:
                status = int(status)
            else:
                status = 200

            return _corsify_actual_response(jsonify(response)), status
    except Exception as e:
        print(e)
        final_json = {"error": "Something Went Wrong", "status": 500}
        return _corsify_actual_response(jsonify(final_json)), 500


if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=8080)


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
