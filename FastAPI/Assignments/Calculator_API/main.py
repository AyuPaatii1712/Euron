from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .calculation import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

fastapps = FastAPI()

class CalculatorModel(BaseModel):
    a: int
    b: int
    operator: str
    
@fastapps.post("/calculator")
def calculator(model: CalculatorModel):
    if model.operator.lower() in ("add", "+"):
        return add_numbers(model)
    elif model.operator.lower() in ("sub", "subtract", "-"):
        return subtract_numbers(model)
    elif model.operator.lower() in ("mul", "multiply", "*"):
        return multiply_numbers(model)
    elif model.operator.lower() in ("div", "divide", "/"):
        return divide_numbers(model)
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    