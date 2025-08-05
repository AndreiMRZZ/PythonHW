from flask import request, jsonify
from functools import wraps

VALID_TOKEN = "secret123"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Invalid or missing header"}), 401

        token = auth_header.split(" ")[1]  #extrag tokenul

        if token != VALID_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401

        #daca e ok totul se ruleza functia normal
        return f(*args, **kwargs)

    return decorated