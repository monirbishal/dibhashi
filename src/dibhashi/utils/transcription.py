from transformers import pipeline
import torch

def transcribe_audio(audio_path):
    """
    Transcribes the given audio file to text using OpenAI's Whisper model.

    Parameters:
    - audio_path (str): Path to the audio file.

    Returns:
    - str: Transcribed text.
    """
    # Determine the device to run the model on
    device = 0 if torch.cuda.is_available() else -1

    # Initialize the ASR pipeline with the Whisper model
    asr_pipeline = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-small",
        device=device,
        return_timestamps=True
    )

    # Transcribe the audio file
    result = asr_pipeline(audio_path)

    # Return the transcribed text
    return result["text"]
