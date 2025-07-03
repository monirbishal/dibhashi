import os
import subprocess
import yt_dlp

def download_and_trim_media(media_url: str, output_dir: str, start: int = 0, duration: int = 30) -> dict:
    """
    Downloads and trims audio & video from a supported media URL—
    saving them into `output_dir` and trimming each to the given duration.

    Returns:
      dict:
        {
          'audio': input-trimmed-audio.mp3,
          'video': input-trimmed-video.mp4
        }
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define file paths
    tmp_video = os.path.join(output_dir, 'temp.mp4')
    final_video = os.path.join(output_dir, 'input-trimmed-video.mp4')
    final_audio = os.path.join(output_dir, 'input-trimmed-audio.mp3')

    # yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': tmp_video,
        'quiet': False,
        'merge_output_format': 'mp4',  # Ensure merging of video and audio
    }

    # Download media using yt-dlp
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([media_url])
    except Exception as e:
        print(f"Error downloading media: {e}")
        return {}

    # Trim video using ffmpeg
    try:
        subprocess.run([
            'ffmpeg', '-y',
            '-ss', str(start),
            '-i', tmp_video,
            '-t', str(duration),
            '-c', 'copy',
            final_video
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error trimming video: {e.stderr.decode()}")
        return {}

    # Extract audio from the trimmed video
    try:
        subprocess.run([
            'ffmpeg', '-y',
            '-i', final_video,
            '-vn',
            '-acodec', 'libmp3lame',
            '-ab', '192k',
            final_audio
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e.stderr.decode()}")
        return {}

    # Clean up the temporary video file
    try:
        os.remove(tmp_video)
    except OSError as e:
        print(f"Error removing temporary file: {e}")

    return {'audio': final_audio, 'video': final_video}
