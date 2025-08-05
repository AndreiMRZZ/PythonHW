from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.services.factorial_service import factorial_calc
from app.storage.db import save_requests
from app.models.math import FactorialRequest
from app.utils.auth import token_required
from app.utils.event_logger import send_log
from app.utils.response import handle_response

factorial_bp = Blueprint('factorial', __name__)


@factorial_bp.route("/factorial", methods=["POST"])
@token_required
def factorial_route():
    try:
        data = request.get_json() #preia json
        factorial_request = FactorialRequest(**data) #validam inputurile
    except(ValidationError, TypeError) as e1:
        return jsonify({"error": str(e1)}), 400

    try:
        result = factorial_calc(factorial_request.n)
    except ValueError as e2:
        return jsonify({"error": str(e2)}), 400 #in cazul in care este nr negativ

    send_log("factorial", {
        "n": factorial_request.n,
        "result": result
    })

    return handle_response("factorial", factorial_request.n, None, result)
#model de raspuns