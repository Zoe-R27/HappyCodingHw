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
def get_persons():
    return personDB

# 幫助函數 - 在personDB從一個id,找到一個Person
# 返回Person的index，如果沒有找到返回-1
def findPerson(pid):
  for i in range(len(personDB)):
    if personDB[i].id == pid:
      return i
  return -1

# 第二個READ函數，返回一個的Person
@app.get("/Person/{person_id}")
def get_person(person_id: int):
  index = findPerson(person_id)
  if index > -1:
    return personDB[index]
  return {"message": "That person is not in the database 這個人不在資料庫裏"}

# 第一個Create函數，把新的Person的oject加入在personDB裏
@app.post("/Add_Person_Item")
def add_person_item(person: Person):
  index = findPerson(person.id)
  if index == -1: # 如果人已經在資料庫，會改變人的消息
    update_person_item(person)
  personDB.append(person)
  return {"message": "Person added 人加入了"}

# 第二個Create函數，如果沒有Person的object，還可以加入人
@app.post("/Add_Person")
def add_person(id: int, name: str, age: int, nat: str, time: Optional[datetime] = datetime.now()):
  data = {
    "id": id,
    "Name": name,
    "Age": age,
    "Nationality": nat,
    "created_time": time
  }
  tempPerson = Person(**data) # 把人的消息改成Person的oject
  # print(tempPerson)
  return (add_person_item(tempPerson)) # 用已經寫的函數來加入人的消息

# 第一個Update函數，會改變人的消息
@app.put("/Update_Person_Item")
def update_person_item(person: Person):
  index = findPerson(person.id)
  if index != -1:
    personDB[index] = person
    return {"message": "Person has be updated 人的消息改變了"}
  return {"message": "Person does not exist in the database 人不在資料庫裏"}

# 第二個Update函數，如果沒有Person的object，還可以改變
@app.put("/Update_Person")
def update_person(id: int, name: str, age: int, nat: str, time: Optional[datetime] = datetime.now()):
  data = {
    "id": id,
    "Name": name,
    "Age": age,
    "Nationality": nat,
    "created_time": time
  }
  tempPerson = Person(**data)
  return (update_person_item(tempPerson))

# 第一個Delete函數，把一個Person的object刪除了
@app.delete("/Delete/{person_id}")
def delete_person(pid: int):
  index = findPerson(pid)
  if index != -1:
    personDB.pop(index)
    return {"message": "Person deleted 人刪除了"}
  return {"message": "Person does not exist in the database 人不在資料庫裏"}

# 第二個Delete函數，每個Person的objects刪除了
@app.delete("/Delete")
def delete_all():
  personDB.clear
  return {"message": "Deleted all people from database 每個人都刪除了"}
