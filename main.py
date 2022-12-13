# import whisper

# import models
# from worker import Worker
# from models import Task

# from params.create_task import CreateTask

# from fastapi import FastAPI

# with models.base_model.db:
#     models.base_model.db.create_tables([Task])

# worker = Worker()
# app = FastAPI()

# worker.start()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/tasks/{item_id}")
# def read_item(item_id: int, q: None):
#     return {"item_id": item_id, "q": q}


# @app.post("/tasks")
# def create(task: CreateTask):
#     Task.create(source_url=task.source_url)
#     return task

# model = whisper.load_model("base")
# result = model.transcribe("audio.mp3")
# print(result)

import uuid
from services.playlist_selector import PlaylistSelector
from services.hls_audio_converter import HlsAudioConverter
from services.transcript_generator import TranscriptGenerator
from services.caption_generator import CaptionGenerator

namespace = str(uuid.uuid4())

source_url = "https://nsm-video.netshow.me/6e9ef96b-249f-4ecc-91e0-ac6d70c34bb5/b4b88a3c-a16e-497c-976c-8d5d0109dd07/playlist.m3u8"
selector = PlaylistSelector(source_url)
playlist_selected = selector.execute()

converter = HlsAudioConverter(playlist_selected, namespace)
audio_full_path = converter.execute()

transcript_generator = TranscriptGenerator(audio_full_path)
segments = transcript_generator.execute()

caption_generator = CaptionGenerator(segments, namespace)
captions = caption_generator.execute()

