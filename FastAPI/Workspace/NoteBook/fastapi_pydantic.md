
# FastAPI – Pydantic Models and Type Hints in API Requests

## ❓ Question 1:  
**In APIs we're passing the data in JSON format then how it gets converted into the class object, is it a property of FastAPI that request goes into class object. and the class object is same as that we've passed as datatype of function parameter?**

### ✅ Answer:
Yes — this is a property of **FastAPI** (powered by **Pydantic**).

Here’s what happens:

1. A client sends JSON:
   ```json
   {
     "a": 10,
     "b": 5,
     "operation": "add"
   }
   ```

2. FastAPI:
   - Reads the request body as JSON  
   - Parses it into a Python dict  
   - Passes it to the **Pydantic model** (`Calculation`)  
   - Pydantic validates types and required fields  
   - If valid, FastAPI creates an **instance** of the model and injects it into your endpoint function  

Example:
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculation(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculate")
def calculate(data: Calculation):
    print(type(data))      # <class 'Calculation'>
    print(data.dict())     # {'a': 10.0, 'b': 5.0, 'operation': 'add'}
    return {"result": data.a + data.b}
```

So when you call the endpoint, the `data` parameter is **exactly the class object** you declared (`Calculation`), with validated fields.

---

## ❓ Question 2:  
**If we don't pass any data type then what will happen?**

### ✅ Answer:
The behavior changes depending on how you declare the parameter:

### Case 1: With a Pydantic class
```python
@app.post("/calculate")
def calculate(data: Calculation):
    ...
```
➡️ FastAPI reads the JSON body, validates it, and converts it into a `Calculation` object.

---

### Case 2: No type hint
```python
@app.post("/calculate")
def calculate(data):
    return {"data": data}
```
➡️ FastAPI does **not** look at the JSON body.  
It assumes `data` should come from **query parameters**.  
If you send JSON, `data` will be `None`.  

To manually access the body:
```python
from fastapi import Request

@app.post("/calculate")
async def calculate(request: Request):
    body = await request.json()
    return {"data": body}
```

---

### Case 3: Basic Python types
```python
@app.post("/calculate")
def calculate(a: int, b: int):
    return {"result": a + b}
```
➡️ FastAPI assumes these are **query parameters** (`/calculate?a=10&b=5`).  
It does not parse them from JSON unless you explicitly use `Body(...)` or a Pydantic model.

---

### 🔑 Summary
- **With Pydantic model** → JSON body → validated → converted to class instance  
- **Without type hint** → Treated as query params, JSON ignored  
- **With basic types** → Taken from query params by default  
- To parse JSON manually without Pydantic → use `Request.json()`  

---
