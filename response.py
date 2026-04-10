from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel,Field

#响应类型
"""
1. json
2. html
3. text
"""
app = FastAPI()


#html 响应装饰器中响应
from fastapi.responses import HTMLResponse,FileResponse
@app.get("/html",response_class=HTMLResponse)
async def get_html():
    return '<h1>hello world</h1>'

#返回文件内容，如图片、PDF\excel,音视频等
@app.get("/file")
async def get_file():
    file_path = '.\\files\\image.png'
    return FileResponse(file_path)

"""
自定义响应数据格式
"""
class Book(BaseModel):
    bookname: str
    author: str
    price: float

@app.get("/book/{id}",response_model=Book)
async def get_book(id: int):
    return {"bookname": "python", "author": "hui", "price": 10.0}


#异常处理，对于客户端引发的错误，应使用fastapi.HTTPException来中断正常处理的流程，并返回标准的错误响应
from fastapi import HTTPException
@app.get("/news/{id}")
async def get_news(id: int):
    id_list = [1,2,3,4,5]
    if id not in id_list:
        raise HTTPException(status_code=404,detail="新闻不存在")
    return {"id": id}


if __name__ == '__main__':
    uvicorn.run(app='response:app',host='127.0.0.1',port=8000,reload=True)    
