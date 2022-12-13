from datetime import timedelta
from typing import List


class CaptionGenerator:
    def __init__(self, segments: List, namespace: str):
        self.segments = segments
        self.namespace = namespace

    def execute(self) -> List:
        captions = []

        for segment in self.segments:
            start_time = str(
                0)+str(timedelta(seconds=int(segment['start'])))+',000'
            end_time = str(
                0)+str(timedelta(seconds=int(segment['end'])))+',000'

            text = segment['text']

            segment_id = segment['id']+1
            segment = f"{segment_id}\n{start_time} --> {end_time}\n{text[1:] if text[0] is ' ' else text}\n\n"

            captions.append(segment)

        with open("caption.srt", 'w', encoding='utf-8') as srt:
            for caption in captions:
                 srt.write(caption)


        return caption
