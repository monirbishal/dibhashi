from banglatts import BanglaTTS
import os

def bangla_text_to_speech(
        bn_text: str, 
        output_dir: str,
        voice: str = 'female', 
        filename: str = 'output_audio.wav', 
    )-> dict:
    """
    Converts Bangla text to speech using BanglaTTS and saves the output audio file.

    Parameters:
        text (str): Bangla text to convert to speech.
        voice (str): Voice gender to use ('male' or 'female').
        filename (str): Desired filename for the output audio (with extension).
        output_dir (str): Directory where the audio file will be saved.

    Returns:
        str: Path to the saved audio file.
    """

    tts = BanglaTTS()
    output_path = os.path.join(output_dir, filename)

    # Generate speech and save to the file
    tts(bn_text, voice=voice, filename=output_path)
    
    
    return output_path
