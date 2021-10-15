from fastapi import FastAPI # Import Fast API
from pydantic import BaseModel # Import data validation
from datetime import datetime
from typing import Optional
app = FastAPI() # Create FastAPI instance

# 在這個作業，我會用Python的list (串列)來存儲消息
personDB = []

# Python class，代表資料庫的欄
class Person (BaseModel):
  id: int # 我會說這是Primary Key
  Name: str
  Age: int
  Nationality: str
  created_time: datetime = datetime.now()

# 第一個READ函數 （function)，返回personDB的内容
@app.get("/Persons")
async def get_persons():
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
async def get_person(person_id: int):
  index = findPerson(person_id)
  if index > -1:
    return personDB[index]
  return {"message": "That person is not in the database 這個人不在資料庫"}

# 第一Create函數，把新的Person消息加入在personDB裏
@app.post("/Add_Person")
async def add_person(id: int, name: str, age: int, nat: str, time: Optional[datetime] = datetime.now()):
  


# @app.update
#
# @app.delete
