
from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World556"}


@app.get("/hello/")
async def say_hello():
    return {"message": f"Hello wanghui"}


@app.get("/book/{id}")
async def get_book(id: int):
    return {"id": id,"str":f"这是第{id}本书"}


#请求体参数
from pydantic import BaseModel
class User(BaseModel):
    username: str
    password: str

class Book(BaseModel):
    bookname: str
    author: str
    price: float
    publisher: str
@app.post("/book/")
async def create_book(book: Book):
    return {"bookname": book.bookname,
            "author":book.author,
            "price":book.price,
            "publisher":book.publisher
}
#请求体参数-类型注解Field
from pydantic import BaseModel, Field
class User(BaseModel):
    username: str = Field(...,min_length=4,max_length=10,title="用户名",description="用户名长度4-10")
    password: str = Field(...,min_length=6,max_length=20,title="密码",description="密码长度6-20")
    
@app.post("/login/")
async def login(user: User):
    return {"username": user.username}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
