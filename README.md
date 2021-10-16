# 郴弄梅 - Zoe Rudd - 快樂學程式 - 面試作業
### 標準：
用FASTAPI，編寫一個REST API，有CRUD的部分 （Create, Read, Update, Delete)

### 我用的軟體：
  - Atom
  - GitHub
  - Ubuntu Linux Subsystem on Windows

### 怎麽用：
1. 首先，clone這個Github的repository
2. 第二，在terminal上，`uvicorn main:app`來運行實時服務器 
3. 第三，打開`http://localhost:8000/docs`，您可以看到FASTAPI的auto-generated docs，更容易測試這個API的功能性
4. 選擇一個函數，加入您想要的消息

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
4. 我認爲用MYSQL資料庫很複雜，有一點麻煩，因爲需要設置其他的軟體（比如：SQLAcdemy)，所以在第一迭代我不會用來可以注意學習FASTAPI. 我會用Python的串列來存儲消息
5. 我開始編寫程式: 編寫程式的時候，我常常看這些網站來幫我寫對的。我也常常查一些Python的syntax
  - 開始編寫程式的時候，我也創造新的Github repository，所以我可以開始追蹤我的進程
  - 首先用FASTAPI Introduction網站的例子來試試怎麽用FASTAPI 和 uvicorn
  - 其次開始寫自己的程式，選擇在那個迭代不會用MySQL資料庫，會用Python串列
  - 然後選擇我的資料庫内容的例子是人們的消息, 寫`personDB`的變數和`Person`的class
  - 然後寫第一個READ的函數，選擇我應該有兩個READ函數，所以人們可以找一個人或者存取每個人的消息
  - 然後我寫一個Create和Update函數，在這兩函數您可以加入人的消息，但是我也想加入Person的object的能力所以我寫了第二個Create和Update函數
  - 因爲我在第二個Create和Update的函數調用第一個Create和Update的函數，我不可以用async的函數所以我把async函數改變普通函數
  - 最後，我寫了兩個Delete函數
6. 編寫程式的時候，同時寫comments,所以我和其他的人可以知道我做什麽
7. 我寫完README

### 我的挑戰，問題，而怎麽解決
1. 學習FASTAPI是什麽 - 我去看很多網站和視頻
2. 選擇應不應該用MySQL資料庫 - 我選擇不應該用，因爲我想注意好好學習FASTAPI。用MySQL資料庫會讓我有更多不瞭解的問題
3. 應該編寫怎麽樣的資料庫，因爲標準只是用FASTAPI編寫有CRUD的Rest API - 我認爲應該用比較簡單的資料庫有關的結構，因爲我想重視學習FASTAPI，所以我選用Python的串列。我也選擇應該用比較簡單的消息，所以我寫了人的消息class。這個class很容易瞭解。
4. 我忘記了一些Python的Syntax - 因爲我最近用的程式語言是Go，我忘記了一些Python的Syntax，所以我需要去看一些學習Python的網站（我很喜歡的網站是[W3Schools](https://www.w3schools.com/python/) 和 [GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/))。所以不是很大的問題，只是我需要花了一些時間去查一下。
5. 我有一些Ubuntu和GitHub的問題 - 因爲我很長時間沒用Ubuntu，我需要update和upgrade它，我也需要下載FASTAPI，uvicorn和pip，但是uvicorn的path有一些問題，所以我去看一些網站。看完以後，我可以解決我的問題。GitHub也有一些問題因爲這是我第一次用自己的GitHub（以前，我用我的學校或者公司GitHub），但看一些網站以後，我沒有問題。
