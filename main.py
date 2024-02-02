import streamlit as st
from pytube.exceptions import RegexMatchError
from Downloader import Downloader

def load_frontend():
    tab1, tab2 = st.tabs(["Audio Only", "Audio + Video(N/A)"])
    form = st.empty()
    with form:
        with st.form("test_form"):
            video_url = st.text_input("Url")
            run_button = st.form_submit_button("Lock video")

    with tab1: #Audio Only
        if run_button:
            try:
                downloader = Downloader(video_url)
                audio_stream = downloader.get_audio_stream()
                st.image(f"{downloader.thumbnail_url}", caption=f"{downloader.title}", width=300)
                download_button = st.button("Download")
                form.empty()
                if download_button:
                    audio_stream.download(output_path='./downloads')
            except RegexMatchError:
                st.warning('Incorrect Url', icon="⚠️")

    with tab2:
        pass
    
    
    
    


def main():
    load_frontend()

if __name__ == '__main__':
    main()