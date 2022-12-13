import whisper

import models
from worker import Worker
from models import Task

from params.create_task import CreateTask

from fastapi import FastAPI

with models.base_model.db:
    models.base_model.db.create_tables([Task])

worker = Worker()
app = FastAPI()

worker.start()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tasks/{item_id}")
def read_item(item_id: int, q: None):
    return {"item_id": item_id, "q": q}


@app.post("/tasks")
def create(task: CreateTask):
    Task.create(source_url=task.source_url)
    return task



