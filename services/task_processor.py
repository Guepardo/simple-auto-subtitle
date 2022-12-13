import uuid
import os
from typing import List
from models import Task
from utils import shell

from services.playlist_selector import PlaylistSelector
from services.hls_audio_converter import HlsAudioConverter
from services.transcript_generator import TranscriptGenerator
from services.caption_generator import CaptionGenerator


class TaskProcessor:
    ROOT_STORAGE_DIR = 'storage'
    ROOT_TEMP_DIR = 'tmp'

    def __init__(self, task: Task):
        self.task = task
        self.namespace = str(uuid.uuid4())

    def execute(self) -> str:
        playlist = self.select_playlist()
        full_audio_path = self.convert_hls_to_mp3(playlist)
        segments = self.generate_transcript(full_audio_path)
        self.generate_caption(segments)

        self.clean()

        return self.namespace

    def select_playlist(self) -> str:
        selector = PlaylistSelector(self.task.source_url)
        return selector.execute()

    def convert_hls_to_mp3(self, playlist: str) -> str:
        converter = HlsAudioConverter(playlist, self.namespace)
        return converter.execute()

    def generate_transcript(self, audio_full_path: str) -> List:
        transcript_generator = TranscriptGenerator(audio_full_path)
        return transcript_generator.execute()

    def generate_caption(self, segments: List) -> None:
        caption_generator = CaptionGenerator(
            segments, self.ROOT_STORAGE_DIR, self.namespace)
        caption_generator.execute()

    def clean(self):
        shell(f"rm -rf { os.path.join(self.ROOT_TEMP_DIR, self.namespace) }*")
