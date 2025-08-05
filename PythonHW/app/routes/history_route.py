from flask import jsonify, Blueprint
from app.storage.db import get_all_requests
from app.utils.auth import token_required
from app.utils.event_logger import send_log

history_bp = Blueprint('history', __name__)


@history_bp.route("/history", methods=["GET"])
def history():
    request = get_all_requests()

    return jsonify({
        "total": len(request),
        "request": request
    }), 200
