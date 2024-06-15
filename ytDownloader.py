import ssl
import certifi
from pytube import YouTube

# Configure SSL context to use certifi's certificates
ssl._create_default_https_context = ssl._create_unverified_context

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get all streams
    streams = yt.streams.filter(progressive=True)

    # Select the highest resolution stream
    highest_resolution = None
    for stream in streams:
        if highest_resolution is None or int(stream.resolution[:-1]) > int(highest_resolution.resolution[:-1]):
            highest_resolution = stream

    # Download the highest resolution stream
    highest_resolution.download()

    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
