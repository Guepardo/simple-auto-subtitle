from typing import Any, List
import whisper


class TranscriptGenerator:
    MODEL_TYPE = 'base'

    def __init__(self, full_path: str):
        self.full_path = full_path
        self.model = whisper.load_model(self.MODEL_TYPE)

    def execute(self) -> List:
        result = self.model.transcribe(self.full_path, fp16=False)
        return result['segments']
