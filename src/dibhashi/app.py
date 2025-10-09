"""
Copyright 2025 Monir Hossain

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


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

@app.route('/audio-to-text', methods=['GET', 'POST'])
def audioToText():
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
                return render_template('audio-to-text.html', error=error, session_id=session_id, transcription=transcription)
            except Exception as e:
                error = f'Error: {str(e)}'
                return render_template('audio-to-text.html', error=error)
        else:
            error="No URL provided."
    else:
        return render_template('audio-to-text.html', error=error)
    
@app.route('/translate-text-en-to-bn', methods=['GET', 'POST'])
def translateTextEnToBn():
    error = ""
    if request.method == 'POST':
        en_text = request.form.get('en_text')
        if en_text:
            try:
                bn_text = en_to_bn(en_text)
                if bn_text:
                    return render_template('translate-en-to-bn.html', error=error, en_text=en_text, bn_text=bn_text)
                else:
                    error = "Error during translation."
                return render_template('translate-en-to-bn.html', error=error, en_text=en_text,)
            except Exception as e:
                error = f'Error: {str(e)}'
                return render_template('translate-en-to-bn.html', error=error)
        else:
            error="No text provide."
    else:
        return render_template('translate-en-to-bn.html', error=error)
    
# @app.route('/traning-model')
# def traningModel():
#     traning_model()

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/docs', methods=['GET'])
def docs():
    return render_template('docs.html')


def main():
    # Production vs Development configuration
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5002))
    host = os.getenv('HOST', '0.0.0.0')
    
    app.run(host=host, port=port, debug=debug_mode)

if __name__ == '__main__':
    main()
