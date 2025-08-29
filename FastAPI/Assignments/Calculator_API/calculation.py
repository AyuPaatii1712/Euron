from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CalculationModel(BaseModel):
    a: int
    b: int

@app.post("/add")
def add_numbers(model: CalculationModel):
    def add(a, b):
        return a + b
    
    result = add(model.a, model.b)
    return {"result": result}

@app.post("/subtract")
def subtract_numbers(model: CalculationModel):
    def subtract(a, b):
        return a - b
    
    result = subtract(model.a, model.b)
    return {"result": result}

@app.post("/multiply")
def multiply_numbers(model: CalculationModel):
    def multiply(a, b):
        return a * b
    
    result = multiply(model.a, model.b)
    return {"result": result}

@app.post("/divide")
def divide_numbers(model: CalculationModel):
    def divide(a, b):
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return a / b
    
    result = divide(model.a, model.b)
    return {"result": result}
