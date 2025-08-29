from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/add")
def add(a:int, b:int):
    return a + b

class SubtractRequest(BaseModel):
    a: int
    b: int

@app.post("/subtract")
def subtract_numbers(model: SubtractRequest):
    def subtract(a, b):
        return a - b
    
    result = subtract(model.a, model.b)
    return {"result": result}

# Run Command: uvicorn test:app --reload --> unicorn [filename]:[app variable name] --reload
# If you are not in the same directory then "API_Examples.test" in place of "test"

# To host the url to public download "ngrok" app and then Extract it and then on CMD run the command i.e. ngrok http 8000 --> ngrok [protocol] [port number]
# It will give you a public URL which you can share with anyone to access your local server