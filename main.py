from fastapi import FastAPI ## Import Fast API
from pydantic import BaseModel ## Import data validation
from datetime import datetime
app = FastAPI() ## Create FastAPI instance

## 在這個作業，我會用Python的list (串列)來存儲消息
db = []

## Python class，代表資料庫的欄
class Person (BaseModel):
  id: int # 我會說這是Primary Key
  Name: str
  Age: int
  Nationality: str

@app.get("/")
def first_example():
  """
  GFG Example First Fast API Example
  """
  return {"GFG Example": "FastAPI"}

@app.get

@app.post

@app.update

@app.delete
