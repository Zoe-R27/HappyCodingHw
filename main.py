from fastapi import FastAPI # Import Fast API
from pydantic import BaseModel # Import data validation
from datetime import datetime
app = FastAPI() # Create FastAPI instance

# 在這個作業，我會用Python的list (串列)來存儲消息
personDB = []

# Python class，代表資料庫的欄
class Person (BaseModel):
  id: int # 我會說這是Primary Key
  Name: str
  Age: int
  Nationality: str

# 第一個READ函數 （function)，返回personDB的内容
@app.get("/Persons")
def get_persons():
    return personDB

# 幫助函數 - 在personDB從一個id,找到一個Person
# 返回Person的index，如果沒有找到返回-1
def findPerson(pid):
  for i in range(len(personDB)):
    if personDB[i].id == pid:
      return i
  return -1

# 第二個READ函數，返回具體的Person
@app.get("/Person/{person_id}")
def get_person(person_id: int):


@app.post

@app.update

@app.delete
