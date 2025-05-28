import subprocess
import os
import yt_dlp

def download_and_trim_audio(yt_url, output_dir='src/dibhashi/static/downloads', trimmed_filename='trimmed_audio.mp3', duration=30):
    """
    Downloads audio from a YouTube video and trims it to the specified duration.

    Parameters:
    - yt_url (str): URL of the YouTube video.
    - output_dir (str): Directory to save the downloaded and trimmed audio.
    - trimmed_filename (str): Filename for the trimmed audio.
    - duration (int): Duration in seconds to trim the audio.

    Returns:
    - str: Path to the trimmed audio file.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Temporary filename for the downloaded audio
    temp_audio_path = os.path.join(output_dir, 'temp_audio.%(ext)s')
    trimmed_audio_path = os.path.join(output_dir, trimmed_filename)

    # yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_audio_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'noplaylist': True,
    }

    # Download audio using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(yt_url, download=True)
        downloaded_file = ydl.prepare_filename(info_dict)
        # Replace extension with .mp3
        base, _ = os.path.splitext(downloaded_file)
        downloaded_file = base + '.mp3'

    # Check if the downloaded file exists
    if not os.path.exists(downloaded_file):
        raise FileNotFoundError(f"Downloaded file not found: {downloaded_file}")

    # Trim the audio using ffmpeg
    subprocess.run([
        'ffmpeg',
        '-y',  # Overwrite output file if it exists
        '-i', downloaded_file,
        '-t', str(duration),
        '-c', 'copy',
        trimmed_audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Remove the temporary audio file
    os.remove(downloaded_file)

    return trimmed_audio_path
