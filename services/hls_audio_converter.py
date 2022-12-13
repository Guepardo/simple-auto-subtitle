import os
from utils import shell


class HlsAudioConverter:
    ROOT_TMP_DIR = 'tmp'

    def __init__(self, playlist_uri, namespace):
        self.playlist_uri = playlist_uri
        self.namespace = namespace

    def execute(self) -> str:
        base_path = os.path.join(self.ROOT_TMP_DIR, self.namespace)
        full_path = os.path.join(base_path, 'audio_source.mp3')

        shell(f"mkdir {base_path}")
        shell(f"ffmpeg -i {self.playlist_uri} {full_path}")

        return full_path
