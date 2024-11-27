import yt_dlp


def download_youtube_video():
    try:
        # Ask the user for the YouTube video URL
        url = input("Enter the YouTube video URL: ")

        # Set download options
        ydl_opts = {
            "format": "best", 
            # Download the best quality video and audio
            "outtmpl": "%(title)s.%(ext)s",  
            # Save with the video title as the filename
        }

        # Create a yt-dlp downloader
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nDownloading...")
            ydl.download([url])  # Download the video
            print("\nDownload completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


download_youtube_video()
