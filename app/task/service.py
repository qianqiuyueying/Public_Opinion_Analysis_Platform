from .model.dto import *
from .respository import *
from util.tool import *
from rdb import *
from typing import List
from fastapi import HTTPException

class scrapyService:
    """
    任务模块的服务层
    """
    def get_task(self, **conditions) -> TaskDTO:
        ...