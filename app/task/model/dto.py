from pydantic import BaseModel, ConfigDict
from typing import Optional


class TaskDTO(BaseModel):
    """
    任务数据传输对象
    """
    id: Optional[int] = None
    user_id: int | None
    spider_list: list | None
    status: str | None
    created_at: str | None
    update_at: str | None