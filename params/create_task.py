from pydantic import BaseModel


class CreateTask(BaseModel):
    source_url: str
