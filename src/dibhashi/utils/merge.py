import os
import subprocess
from dibhashi.utils.utils import get_existing_session_dir

def merge_audio_video(session_id: str) -> str:
    folder = get_existing_session_dir(session_id)
    video_in = os.path.join(folder, "input-trimmed-video.mp4")
    audio_in = os.path.join(folder, "output_audio.wav")  # ensure correct name
    merged_out = os.path.join(folder, "merged_output.mp4")

    if not os.path.exists(video_in) or not os.path.exists(audio_in):
        raise FileNotFoundError("Missing audio or video input file")

    subprocess.run([
        "ffmpeg", "-y",
        "-i", video_in,
        "-i", audio_in,
        "-map", "0:v:0",     # explicitly select video
        "-map", "1:a:0",     # explicitly select audio
        "-c:v", "copy",      # copy video without re-encoding
        "-c:a", "aac",       # re-encode audio as AAC for MP4 compatibility :contentReference[oaicite:2]{index=2}
        "-shortest",         # stop when the shorter stream ends :contentReference[oaicite:3]{index=3}
        merged_out
    ], check=True)

    return merged_out
