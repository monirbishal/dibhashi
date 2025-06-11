import torch
from TTS.api import TTS

def custom_tts(
        bn_text: str,
        output_dir: str,
        reference_audio_path: str):
    # 🧠 Initialize the multilingual voice-cloning model
    # tts = TTS("tts_models/multilingual/multi-dataset/your_tts", progress_bar=True)
    tts = TTS("tts_models/bn/custom/vits-male", progress_bar=True)


    # 🔄 Choose device: GPU if available, else CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts.to(device)

    # --------- INPUT ---------
    # bn_text = "We have not taken any party decision on this issue [election in early April] yet. We hope that the government will consider this issue in light of reality, he says"  # Already translated Bangla text
    # bn_text = "লন্ডনে বিএনপির ভারপ্রাপ্ত চেয়ারম্যান তারেক রহমানের সঙ্গে বৈঠকে বসতে যাচ্ছেন যুক্তরাজ্য সফররত প্রধান উপদেষ্টা ড. মুহাম্মদ ইউনূস। শুক্রবার (১৩ জুন) স্থানীয় সময় সকাল ৯টা থেকে ১১টার মধ্যে এই বৈঠক হবে বলে জানিয়েছেন বিএনপি মহাসচিব মির্জা ফখরুল ইসলাম আলমগীর। আজ মঙ্গলবার (১০ জুন) রাজধানীর গুলশানের রাজনৈতিক কার্যালয়ে সাংবাদিকদের সঙ্গে ঈদ শুভেচ্ছা বিনিময় শেষে এ কথা জানান বিএনপি মহাসচিব।"
    # reference_audio_path = "src/dibhashi/static/downloads/trimmed_media.mp3"  # Supports voice cloning

    # --------- OUTPUT ---------
    output_path = output_dir+"/output_audio.wav"

    # 🎧 Synthesize Bangla speech using the cloned voice
    tts.tts_to_file(
        text=bn_text,
        speaker_wav=reference_audio_path,
        # language="en",        # Bangla language code
        file_path=output_path
    )

    return output_path
