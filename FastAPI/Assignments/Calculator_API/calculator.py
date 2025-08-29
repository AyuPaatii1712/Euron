from typing import Literal
from pydantic import BaseModel

class CalculatorModel(BaseModel):
    a: int
    b: int
    operator: Literal["add", "subtract", "multiply", "divide", "sub", "mul", "div", "+", "-", "*", "/"]