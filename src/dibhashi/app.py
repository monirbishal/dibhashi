from flask import Flask, render_template, request
from dibhashi.utils.download_media import download_and_trim_media
from dibhashi.utils.bangla_tts import custom_tts
from dibhashi.utils.transcription import transcribe_audio
from dibhashi.utils.translation import en_to_bn
from dibhashi.utils.synthesis import bangla_text_to_speech
from dibhashi.utils.merge import merge_audio_video
from dibhashi.utils.utils import make_session_output_dir, get_session_id
from dibhashi.utils.traning import traning_model
import uuid
import os
from dotenv import load_dotenv
# Define the path to .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    error = ""
    if request.method == 'POST':
        media_url = request.form.get('media_url')
        if media_url:
            try:
                audio_path = ""
                session_id = get_session_id()
                output_dir = make_session_output_dir(session_id)
                media_path = download_and_trim_media(media_url, output_dir)
                if media_path['audio']:
                    audio_path = media_path['audio']
                    transcription = transcribe_audio(audio_path)
                    if transcription:
                        bn_text = en_to_bn(transcription)
                        if bn_text:
                            # bn_audio_path = bangla_text_to_speech(bn_text, output_dir)
                            bn_audio_path = custom_tts(bn_text, output_dir, audio_path)
                            if bn_audio_path:
                                merge_audio_video(session_id)
                            else:
                                error = "Error during merging audio into video."
                        else:
                            error = "Error during audio to text."
                    else:
                        error = "Error during audio to text."
                else:
                    error = "Error during download."
                return render_template('index.html', error=error,  session_id=session_id, transcription=transcription, audio_path=audio_path, bn_text=bn_text, bn_audio_path=bn_audio_path)
            except Exception as e:
                error = f'Error: {str(e)}'
                return render_template('index.html', error=error)
        else:
            error="No YouTube URL provided."
    else:
        return render_template('index.html', error=error)

@app.route('/download', methods=['GET', 'POST'])
def download():
    media_url = "https://www.facebook.com/englishwithkrisamerikos/videos/786170160398864/"
    session_id = uuid.uuid4().hex
    download_dir = os.getenv("DOWNLOAD_DIR")
    output_dir = download_dir + "/" + session_id
    outputs = download_and_trim_media(media_url, output_dir)
    return outputs

@app.route('/transcribe', methods=['GET'])
def transcribe():
    audio_path = "src/dibhashi/static/downloads/fa436f1ee5324122b372a8b7d9ec721a/input-trimmed-audio.mp3"
    transcription = transcribe_audio(audio_path)
    return transcription

@app.route('/translate', methods=['GET'])
def translation():
    en_text = "Why are you still speaking English like a robot? In today's world, there's so much great technology, apps, chat GPT that can help you learn the language. But they won't make you fluent. The only way to be fluent is to practice speaking with real people. So I've created a presentation that I want to show you. It is short and quick and will explain how to do this fast. And then I have a program where you can"
    bn_text = en_to_bn(en_text)
    return render_template('index.html', transcription=en_text, bn_text=bn_text)

@app.route('/bn-text-to-audio', methods=['GET'])
def bn_audio():
    session_id = get_session_id()
    output_dir = make_session_output_dir(session_id)
    reference_audio_path = "src/dibhashi/static/downloads/fa436f1ee5324122b372a8b7d9ec721a/input-trimmed-audio.mp3"
    bn_text = "তোমার ইংরেজি এখনও কেন রোবটের মতো শোনায়? আজকের দিনে দুর্দান্ত কিছু টুল—অ্যাপ, ChatGPT—আছে যা ভাষা শিখতে সাহায্য করে। কিন্তু এগুলো তোমাকে সাবলীল করে তুলবে না। সাবলীল হতে হলে প্রকৃত মানুষদের সঙ্গে কথোপকথন চর্চা করতে হবে। এজন্য আমি একটি প্রেজেন্টেশন তৈরি করেছি তোমাকে দেখানোর জন্য। এটা সংক্ষিপ্ত ও স্পষ্ট, এবং এটি তোমাকে দ্রুত শিখতে শেখাবে।"
    # bn_audio_path = bangla_text_to_speech(bn_text, output_dir)
    bn_audio_path = custom_tts(bn_text, output_dir, reference_audio_path)
    # return bn_audio_path
    return render_template('index.html', session_id=session_id, bn_text=bn_text, bn_audio_path=bn_audio_path)


@app.route('/tts', methods=['GET'])
def getTts():
    output = custom_tts()
    return output

@app.route('/watch/<session_id>')
def watch(session_id):
    merged_path = merge_audio_video(session_id)
    # return merged_path
    return render_template('index.html', session_id=session_id)

@app.route('/traning', methods=['GET', 'POST'])
def traning():
    error = ""
    if request.method == 'POST':
        media_url = request.form.get('media_url')
        if media_url:
            try:
                audio_path = ""
                session_id = get_session_id()
                output_dir = make_session_output_dir(session_id)
                media_path = download_and_trim_media(media_url, output_dir, duration=120)
                if media_path['audio']:
                    audio_path = media_path['audio']
                    transcription = transcribe_audio(audio_path)
                else:
                    error = "Error during download."
                return render_template('traning.html', error=error,  session_id=session_id, transcription=transcription)
            except Exception as e:
                error = f'Error: {str(e)}'
                return render_template('traning.html', error=error)
        else:
            error="No YouTube URL provided."
    else:
        return render_template('traning.html', error=error)
    
@app.route('/traning-model')
def traningModel():
    traning_model()


def main():
    app.run(host="0.0.0.0", port=5002, debug=True)

if __name__ == '__main__':
    main()
