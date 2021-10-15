# 郴弄梅 - Zoe Rudd - 快樂學程式 - 面試作業
### 標準：
用FASTAPI，編寫一個REST API，有CRUD的部分 （Create, Read, Update, Delete)

### 我用的軟體：
  - Atom
  - Github
  - Ubuntu Linux Subsystem on Windows

### 我的過程：

1. 我研究FASTAPI, REST API 和CRUD
2. 因爲我沒用過FASTAPI我閲讀一些網站，看一些視頻包括：
  - [FASTAPI Introduction](https://fastapi.tiangolo.com/tutorial/first-steps/)
  - [Pydantic](https://pydantic-docs.helpmanual.io/)
  - [What is a rest api](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
  - [FASTAPI PUT, POST, DELETE](https://www.youtube.com/watch?v=tpT48Rpt-Ww)
  - [FASTAPI, CRUD, REST API, MYSQL](https://www.youtube.com/watch?v=4Zy90rd0bkU)
  - [Python REST APIs with FastAPI, CRUD application](https://dev.to/xarala221/python-rest-apis-with-fastapi-crud-application-9kc)
  - [Building a CRUD APP with FastAPI and MySQL](https://blog.balasundar.com/building-a-crud-app-with-fastapi-and-mysql)
  - [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)
  - [FastAPI Python WebAPI](https://realpython.com/fastapi-python-web-apis/)

3. 我也需要下載FASTAPI，uvicorn, pip等等
4. 我認爲用MYSQL資料庫很複雜，有一點麻煩，因爲需要設置其他的軟體（比如：SQLAcdemy,)，所以在第一迭代我不會用來可以注意學習FASTAPI. 我會用Python的串列存儲消息
5. 我開始編寫程式: 編寫程式的時候，我常常看這些網站來幫我寫對的。我也常常查一些Python的syntax
  - 開始編寫程式的時候，我也創造新的Github repository，所以我可以開始追蹤我的進程
  - 首先用FASTAPI Introduction網站的例子來試試怎麽用FASTAPI 和 unicorn
  - 其次開始寫自己的程式，選擇在那個迭代不會用MySQL資料庫，會用Python串列
  - 然後選擇我的資料庫内容的例子是人們的消息, 寫`personDB`的變數和`Person`的class
  - 然後寫第一個READ的函數，選擇我應該有兩個READ函數，所以人們可以找一個人或者存取每個人的消息
  - 然後我寫一個Create和Update函數，在這兩函數您可以加入人的消息，但是我也想加入Person的object的能力所以我寫了第二個Create和Update函數
  - 因爲我在第二個Create和Update的函數調用第一個Create和Update的函數，我不可以用async的函數所以我把async函數改變普通函數
  

6. 編寫程式的時候，同時寫comments,所以我和其他的人可以知道我做什麽
