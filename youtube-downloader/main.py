from pytube import YouTube

from links import links

# function to download the audio
def download_audio(link, audio_only=True, video_only=False, file_path="./downloads"):
    yt = YouTube(link)
    
    if audio_only:
        yt = yt.streams.get_audio_only()
    else:
        yt = yt.streams.get_highest_resolution()
    
    try:
        print(f"Downloading audio now...\nFile: {yt.default_filename}\nSize: {yt.filesize} bytes")
        yt.download(file_path)
        print(f"Downloaded audio successfully. File name: {yt.default_filename}")
    except:
        print("There was an error downloading the audio.")

# Loop through the links
for link in links:
    download_audio(link, audio_only=True)
