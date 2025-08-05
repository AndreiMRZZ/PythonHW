from app.models.record import RequestRecord
from app.storage.db import save_requests
from flask import jsonify
from typing import Optional

def handle_response(operation: str, x: float, y: Optional[float], result: float, extra: Optional[dict] = None):
    record = RequestRecord(
        operation=operation,
        input1=x,
        input2=y,
        result=result
    )
    save_requests(record)

    response = {
        "operation": operation,
        "x": x,
        "result": result
    }

    if y is not None:
        response["y"] = y

    if extra:
        response.update(extra)

    return jsonify(response), 200
