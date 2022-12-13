import m3u8
from IPython import embed


class PlaylistSelector:
    def __init__(self, source_url: str) -> None:
        self.source_url = source_url

    def execute(self) -> str:
        main_playlist = m3u8.load(self.source_url)
        playlist_sorted = sorted(
            main_playlist.playlists, key=lambda item: item.stream_info.bandwidth)

        return playlist_sorted[0].absolute_uri
