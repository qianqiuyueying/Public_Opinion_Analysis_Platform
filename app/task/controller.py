from fastapi import APIRouter, Body, Depends, HTTPException, Query, Path, Request, Header
from .model.dto import *
from .service import *
from util.tool import *
import service

task_router = APIRouter(prefix="/task")

@task_router.post("/create")
async def create_task(
    task: TaskDTO = Body(...),
    service = Depends(taskService)
):
    """
    创建任务
    """
    ...
