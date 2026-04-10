"""
中间件
每次进入FASTAPI都会执行的函数，请求前和响应前，中间件自下而上执行

"""
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

"""
中间件是所有接口都会调用
"""
# @app.middleware("http")
# async def middleware1(request, call_next):
#     print("中间件1")
#     response = await call_next(request)
#     print("中间件1结束")

#     return response

# app.middleware("http")
# async def middleware2(request, call_next):
#     print("中间件2")
#     response = await call_next(request)
#     print("中间件2结束")

#     return response
@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
依赖注入，由人为决定共享通用的逻辑，避免代码的重复
1. 创建一个依赖函数，返回一个对象

2. 导入depends
3.声明依赖项

"""
from fastapi import Query,Depends
#分页参数逻辑公用，用户列表和新闻列表
#依赖项
# async def common_params(
#         skip: int = Query(0,description="页码"), 
#         limit: int = Query(10,description="每页数量")
#         ):
# @app.get("/user/user_list")
# async def get_users(common: dict = Depends(common_params)):
#     return {"msg": "用户列表"}

# @app.get("/news/news_list")
# async def get_news(common: dict = Depends(common_params)):
#     return {"msg": "新闻列表"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000,reload=True)

