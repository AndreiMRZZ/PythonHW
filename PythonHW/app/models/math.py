from pydantic import BaseModel, Field


class PowClass(BaseModel):
    x: float = Field(..., description='Base')
    y: float = Field(..., description="Exponent")


# model pydantic pt validarea inputului (trb sa fie un intreg)
class FactorialRequest(BaseModel):
    n: int


class FibonacciRequest(BaseModel):
    n: int = Field(...,ge=0, description="Indexul n in sir >=0")