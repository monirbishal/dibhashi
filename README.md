# AI Video Translator: Translate English Video to Bangla Video

## 🧱 Project Overview
Our application will follow these steps:

1. Input: User submits a YouTube video URL.
2. Audio Extraction: Download and extract the first 30 seconds of audio.
3. Transcription: Convert English audio to text.
4. Translation: Translate English text to Bengali.
5. Text-to-Speech: Convert Bengali text to audio.
6. Video Generation: Combine the new audio with the original video.
7. Output: Display the final video to the user.


# How to setup development enveronment

## Requirements
- Python 3.9
- Poetry (dependency management)
- Some other packages

### 1. Install Poetry
If not already installed:
```bash
    curl -sSL https://install.python-poetry.org | python3 -
```
#### Ensure the Poetry binary is in your path:
```bash
    export PATH="$HOME/.local/bin:$PATH"
```

### 2. Make sure Python 3.9 is available and set it for the project:
```bash
    poetry env use python3.9
```

### 3. Configure Poetry to Use Virtual Environments In-Project directory:
```bash
    poetry config virtualenvs.in-project true
```

### 4. Install Dependencies
```bash
    poetry install
```

#### Install tailwindcss: 
```bash
npm install tailwindcss @tailwindcss/cli --save-dev
```

### 5. Activate the Virtual Environment:
```bash
poetry shell
```

### 6. How Run application:
```bash
poetry run my-script
```

#### How to compile tainwind css: 
```bash
npx tailwindcss -i ./src/dibhashi/static/css/input.css -o ./src/dibhashi/static/dist/output.css --watch
```

### Finaly open in your browser: http://127.0.0.1:5002/