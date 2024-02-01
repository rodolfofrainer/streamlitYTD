import streamlit as st
from pytube.exceptions import RegexMatchError
from Downloader import Downloader

def load_frontend():
    tab1, tab2 = st.tabs(["Audio Only", "Audio + Video"])
    video_url = st.text_input("Url")

    with tab1: #Audio Only
        try:
            downloader = Downloader(video_url)
            streams = downloader.get_audio_stream().download(output_path='./downloads')
        except RegexMatchError:
            print('error')

    with tab2:
        pass
    
    
    
    


def main():
    load_frontend()

if __name__ == '__main__':
    main()