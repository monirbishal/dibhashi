from flask import Flask, render_template, request
from dibhashi.utils.download_youtube_audio import download_and_trim_audio
from dibhashi.utils.transcription import transcribe_audio
from dibhashi.utils.translation import en_to_bn
import os

app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        if youtube_url:
            try:
                audio_path = download_and_trim_audio(youtube_url)
                transcription = transcribe_audio(audio_path)
                bn_text = en_to_bn(transcription)
                return render_template('index.html', transcription=transcription, audio=audio_path, bn_text=bn_text)
            except Exception as e:
                error = f'Error: {str(e)}'
                return render_template('index.html', error=error)
        else:
            return render_template('index.html', error="No YouTube URL provided.")
    else:
        return render_template('index.html')

@app.route('/translate', methods=['GET'])
def translation():
    en_text = "Hello English learners and welcome back to EnglishPod. My name is Marco and I'm Erica. How are you, Erica? Marco, I'm doing really well today. You're excited. Uh-huh. We've got a great lesson for everyone. Yes. We have a really common situation where we're going to use real English, right? Yep. Everyday English, English that people really use. And that's what we want you to learn. What are we talking about today specifically? Today we have a really common situation that is a little bit embarrassing."
    bn_text = en_to_bn(en_text)

    return render_template('index.html', transcription=en_text, bn_text=bn_text)

def main():
    app.run(host="0.0.0.0", port=5002, debug=True)

if __name__ == '__main__':
    main()
