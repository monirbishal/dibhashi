from banglatts import BanglaTTS
import os

def bangla_text_to_speech(text: str, voice: str = 'female', filename: str = 'output.wav', save_dir: str = 'src/dibhashi/static/downloads') -> str:
    """
    Converts Bangla text to speech using BanglaTTS and saves the output audio file.

    Parameters:
        text (str): Bangla text to convert to speech.
        voice (str): Voice gender to use ('male' or 'female').
        filename (str): Desired filename for the output audio (with extension).
        save_dir (str): Directory where the audio file will be saved.

    Returns:
        str: Path to the saved audio file.
    """
    
    os.makedirs(save_dir, exist_ok=True)

    tts = BanglaTTS()
    output_path = os.path.join(save_dir, filename)

    # Generate speech and save to the file
    tts(text, voice=voice, filename=output_path)
    
    # Generate audio file path
    bn_audio_path = 'downloads/'+filename
    
    return bn_audio_path
