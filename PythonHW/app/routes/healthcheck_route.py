from flask import Blueprint, jsonify
from app.utils.auth import token_required

healthcheck_bp = Blueprint('healthcheck', __name__)


@healthcheck_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "OK"}), 200
