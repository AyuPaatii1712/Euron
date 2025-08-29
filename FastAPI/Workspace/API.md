# Notes

# Types of methods in APIs
1. GET
2. POST
3. PUT
4. DELETE

## 1. GET Method
* In this method the data going to expose into the API 
    - i.e. when we hit any API with the inputs the inputs will be shown into the APIs
    - Example: http://127.0.0.1:8000/add?a=2&b=4 (here we can see that the inputs to this APIs are a=2 and b=4)
* It is not secure way, because the inputs are exposed in APIs

## 2. POST Method
* In this method the data will not expose into the API 
    - Example: http://127.0.0.1:8000/add (the data will be passed separately)
* It is a secure way, In apps we have to use post for data security 

## 3. PUT Method
* It is use to update the whole/complete record, (there is another method i.e. **PATCH** which is used to update the record parcially)
    - Example: http://127.0.0.1:8000/user/update/[user_id](It is the `id` of the record that you want to update) (the record/data will be passed separately)

## 4. DELETE Method
* It is used to delete the record


# Execute the API using `curl`
## GET API
-> curl -i "http://127.0.0.1:8000/add?a=2&b=4" | jq 
    - `-i`: to see the response headers along with the output
    - `| jq`: pretty-printed JSON response (assuming your API returns JSON)

## POST API
-> FastAPI `POST /add` Examples with `curl`

### 1. Using **Query Parameters**

```python
@app.post("/add")
def add(a: int, b: int):
    return {"result": a + b}
```

**curl:**

```bash
curl -X POST "http://127.0.0.1:8000/add?a=2&b=4"
```

---

### 2. Using **Form Data**

```python
from fastapi import Form

@app.post("/add")
def add(a: int = Form(...), b: int = Form(...)):
    return {"result": a + b}
```

**curl:**

```bash
curl -X POST "http://127.0.0.1:8000/add" -d "a=2" -d "b=4"
```

---

### 3. Using **JSON Body**

```python
from pydantic import BaseModel

class Numbers(BaseModel):
    a: int
    b: int

@app.post("/add")
def add(nums: Numbers):
    return {"result": nums.a + nums.b}
```

**curl:**

```bash
curl -X POST "http://127.0.0.1:8000/add" \
     -H "Content-Type: application/json" \
     -d '{"a":2,"b":4}'
```