from pytube import YouTube

class Downloader(YouTube):

        
    def get_audio_stream(self):
        return self.streams.get_audio_only()