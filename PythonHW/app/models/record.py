from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class RequestRecord:
    operation: str
    input1: float
    input2: Optional[float]
    result: float
    timestamp: str = datetime.utcnow().isoformat()
