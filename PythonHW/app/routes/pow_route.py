from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.models.math import PowClass
from app.services.pow_service import pow_calc
from app.storage.db import save_requests
from app.utils.auth import token_required
from app.utils.event_logger import send_log
from app.utils.response import handle_response

pow_bp = Blueprint('pow', __name__)


@pow_bp.route("/pow", methods=["POST"])
@token_required
def pow_route():
    try:
        data = request.get_json() #preia corpul json al cererii
        pow_request = PowClass(**data) #validez inputurile
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400  #daca am eroare returnez 400 bad request, altfel calculez rezultatul

    result = pow_calc(pow_request.x, pow_request.y)

    send_log("pow_request", {
        "x": pow_request.x,
        "y": pow_request.y,
        "result": result
    })


    return handle_response("pow", pow_request.x, pow_request.y, result)