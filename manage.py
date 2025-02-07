from fastapi import FastAPI
import uvicorn
from app.user.controller.userController import user_router


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    return app

app = init_app()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    # app = init_app()
    uvicorn.run('manage:app', host='127.0.0.1', port=8000, reload=True)