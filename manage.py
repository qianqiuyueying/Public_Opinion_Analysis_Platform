from fastapi import FastAPI, Request, HTTPException
import jwt
import uvicorn
from app import init_app
from db import init_db
from config import *




app = init_app()




@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    # app = init_app()
    uvicorn.run('manage:app', host='127.0.0.1', port=8000, reload=True)