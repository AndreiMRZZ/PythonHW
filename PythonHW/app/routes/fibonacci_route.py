from flask import Blueprint, request, jsonify
from app.services.fibonacci_service import fibonacci_calc
from app.storage.db import save_requests
from app.models.math import FibonacciRequest
from app.utils.cache import get_from_cache,save_to_cache
from app.utils.auth import token_required
from app.utils.event_logger import send_log
from app.utils.response import handle_response

fibonacci_bp = Blueprint('fibonacci', __name__)


@fibonacci_bp.route("/fibonacci", methods=["POST"])
@token_required
def fibonacci_route():
    try:
        data = request.get_json()
        fibonacci_request = FibonacciRequest(**data)
    except(ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    result = get_from_cache(fibonacci_request.n)
    # in cazul in care nu exista in cache, il calculez apoi il salvez
    if result is None:
        result = fibonacci_calc(fibonacci_request.n)
        save_to_cache(fibonacci_request.n, result)

    send_log("fiboncci", {
        "n": fibonacci_request.n,
        "result": result
    })

    return handle_response("fibonacci", fibonacci_request.n, None, result)