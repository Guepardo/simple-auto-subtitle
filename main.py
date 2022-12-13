import whisper
import models
import os

from worker import Worker
from models import Task
from fastapi import FastAPI

from playhouse.shortcuts import model_to_dict
from params.create_task import CreateTask
from starlette.responses import FileResponse


with models.base_model.db:
    models.base_model.db.create_tables([Task])

worker = Worker()
app = FastAPI()

worker.start()


@app.get("/tasks/{id}")
def read_item(id: int,):
    task = Task.get(Task.id == id)
    return model_to_dict(task)


@app.post("/tasks")
def create(task: CreateTask):
    task = Task.create(source_url=task.source_url)
    return model_to_dict(task)


@app.get("/captions/{id}")
def get_caption(id: str):
    task = Task.get(Task.id == id)

    file_path = f"{ os.path.join('storage', task.ref_id) }.srt"

    return FileResponse(file_path, media_type='application/octet-stream', filename=f"{task.ref_id}.srt")
