from fastapi import FastAPI ## Import Fast API
app = FastAPI() ## Create FastAPI instance

## 在這個作業，我會用Python的list (串列)來存儲消息

db = []


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
