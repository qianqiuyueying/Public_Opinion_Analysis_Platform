from init import *
from fastapi import FastAPI
from db.init import init_db
import uvicorn

app = init_app()

if __name__ == '__main__':
    # app = init_app()
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)