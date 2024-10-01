from flask import Flask, jsonify, request, make_response
from flask_cors import CORS  # Import CORS
from utils import getOpenAiResponse
app2 = Flask(__name__)

# Enable CORS for all routes
CORS(app2)

@app2.after_request
def remove_server_header(response):
    response.headers.pop("Server", None)
    response.headers.pop("X-Powered-By", None)
    return response

@app2.route("/", methods=['POST', "OPTIONS"])
def process():
    try:
        # Handle the preflight OPTIONS request
        if request.method == "OPTIONS":
            return _build_cors_preflight_response()
        
        # Handle POST requests
        elif request.method == "POST":
            data = request.get_json()
            if not data or 'prompt' not in data:
                return jsonify({"error": "INVALID_REQUEST_BODY"}), 400

            # Assuming getOpenAiResponse returns a valid response
            response = getOpenAiResponse(data['prompt'])
            return jsonify(response), 200

    except Exception as e:
        print(e)
        final_json = {"error": "Something Went Wrong", "status": 500}
        return jsonify(final_json), 500

# Function to build the preflight response
def _build_cors_preflight_response():
    response = make_response("", 200)  # Return a 200 OK status for preflight
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    return response

if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=8080)
