import os
import subprocess
import yt_dlp

def download_and_trim_media(
    media_url: str,
    output_dir: str,
    start: int = 0,
    duration: int = 30,
) -> dict:
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
    # temp_out = os.path.join(output_dir, 'temp_audio.%(ext)s')
    # final_out = os.path.join(output_dir, filename)
    # os.makedirs(output_dir, exist_ok=True)
    
    # 1. Download video + audio together (merged) into tmp.mp4
    tmp_video = os.path.join(output_dir, 'temp.mp4')
    final_video = os.path.join(output_dir, f"input-trimmed-video.mp4")
    final_audio = os.path.join(output_dir, f"input-trimmed-audio.mp3")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': tmp_video,
        'quiet': True,
        # 'noplaylist': True,
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192',
        # }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # info = ydl.extract_info(media_url, download=True)
        # downloaded_path = ydl.prepare_filename(info)
        # downloaded_path = os.path.splitext(downloaded_path)[0] + '.mp3'
        ydl.download([media_url])


    # if not os.path.exists(downloaded_path):
    #     raise FileNotFoundError(f"Audio not found: {downloaded_path}")

    # subprocess.run([
    #     'ffmpeg',
    #     '-y',
    #     '-ss', str(start),
    #     '-i', downloaded_path,
    #     '-t', str(duration),
    #     '-c', 'copy',
    #     final_out
    # ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # try:
    #     os.remove(downloaded_path)
    # except OSError:
    #     pass

    # return final_out

    # 2. Trim video using ffmpeg
    subprocess.run([
        'ffmpeg', '-y',
        '-ss', str(start),
        '-i', tmp_video,
        '-t', str(duration),
        '-c', 'copy',
        final_video
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Extract trimmed audio directly from the trimmed video
    subprocess.run([
        'ffmpeg', '-y',
        '-i', final_video,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '192k',
        final_audio
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 4. Clean up the temp merged file
    try:
        os.remove(tmp_video)
    except OSError:
        pass

    return {'audio': final_audio, 'video': final_video}
