# Dibhashi — English to Bangla AI Video Dubbing Platform

**Dibhashi** is an end-to-end AI-powered platform designed to dub English videos into Bangla, preserving speaker emotion, prosody, and timing through a modular pipeline:

- **ASR** (Automatic Speech Recognition) via Whisper  
- **NMT** (Neural Machine Translation) via fine-tuned transformer model  
- **TTS** (Text-to-Speech) using a voice-cloning VITS model  
- **Audio–Video merger & synchronization** through FFmpeg  

---

## 🚀 Features

- **High-accuracy NMT** via domain-specific fine‑tuning on curated English→Bangla data
- **Modular & extensible backend** using Flask, huggingface/transformers, PyTorch, and essential tools (ffmpeg, pytube/yt-dlp)
- **Advanced voice cloning support** using VITS-based Bangla TTS model for expressive, speaker-conditioned speech (optional)
- **Automated pipeline**: ASR (Whisper) → Translation → TTS → Audio processing → Seamless video dubbing
- **Professional-grade audio processing**: noise reduction, silence trimming/padding, volume normalization for clean outputs
- **Video generation with perfect sync**: leverages ffmpeg for audio merging and duration alignment  
- **Open‑source & research‑friendly**: easy to integrate into your own projects, pipelines, or educational tools


---

## ⚙️ Quick Start — Run Locally 

1. Clone the repo:
    ```bash
    git clone https://github.com/monirbishal/dibhashi.git
    cd dibhashi
    ```

2. Install dependencies (using Poetry or pip):
    ```bash
    poetry install
    # or
    pip install -r requirements.txt
    ```

3. **Run locally**:  
   - See `INSTALL.md` for instructions on launching the Flask backend locally.  
   - Upload a video or use a YouTube link to execute the full pipeline (ASR → NMT → TTS → audio processing → video rendering).

---

🛠️ Need help?  
See `INSTALL.md` for setup details or open an issue in the repo if you hit a snag.

---

## 🧠 How It Works (Pipeline)

1. **Download & Trim**: Uses yt-dlp to download and ffmpeg to trim the first 30 seconds into audio/video files.  
2. **Transcription**: Whisper model transcribes English speech with timestamps.  
3. **Translation**: Fine‑tuned `monirbishal/en-bn-nmt` model translates English → Bangla.  
4. **Speech Synthesis**: VITS-based TTS generates Bangla speech, voice-cloned from reference audio.  
5. **Audio Post-processing**: Volume normalization, silence trimming/padding with pydub.  
6. **Merge & Sync**: ffmpeg merges audio with the trimmed video, ensuring perfect alignment.

---

## 📊 Training & Evaluation

| Epoch | Train Loss | Val Loss | BLEU Score |
|:-----:|:----------:|:--------:|:----------:|
| 1     | 0.2006     | 0.1917   | 24.89      |
| 2     | 0.1334     | 0.1641   | 29.97      |
| 3     | 0.0970     | 0.1544   | **33.15**  |

Final BLEU: **33.15**, showing significant improvement from baseline (~18 BLEU).

Evaluation on test set (via sacreBLEU): **BLEU ≈ 0.075**, with balanced 4‑gram precision and acceptable brevity penalty.

Loss / BLEU training curves are available in the Colab notebook.

---

## 🎯 Target Audience

- AI / ML researchers exploring multilingual speech systems  
- Language learners and educators focusing on Bangla  
- Developers building real-time voice translation or dubbing tools  

---

## 🔧 Future Work

- Support for **multi-speaker voices** and advanced voice cloning  
- Build custom **Bangla ASR** & **TTS** models from scratch  
- Enhance lip-sync via phoneme alignment or AI lip-sync tools  

---

## 📂 Repository Structure

Dibhashi/
├── dibhashi/
│ ├── app.py # Flask API for pipeline
│ ├── pipeline.py # Modular stages (ASR, NMT, TTS, merge)
│ └── utils.py # Helpers: ffmpeg wrappers, audio processing
├── notebooks/
│ └── demo.ipynb # Full Colab walkthrough
├── requirements.txt # Python dependencies
└── README.md

---

## License

This project is licensed under the Apache License 2.0.

You are free to use, modify, and distribute this project under the terms of the license.

See the [LICENSE](LICENSE) file for details.

```
@misc{Dibhashi2025,
author = {Monir Hossain et al.},
title = {Dibhashi: AI‑Powered English to Bangla Video Dubbing Platform},
year = {2025},
howpublished = {GitHub repository},
note = {https://github.com/monirbishal/dibhashi}
}
```

---

## 🙌 Acknowledgments

- **Base NMT model**: `shhossain/opus-mt-en-to-bn` + fine-tuned weights  
- **Whisper ASR** + **VITS TTS** models from Hugging Face  
- Datasets: Tatoeba, BanglaNMT, custom 500+ bilingual pairs  
- Contributors: Md. Monir Hossain, Sadia Sabrina, Abdullah Emon, Ridoy Chandra Dash, Emdadul Haque  
- Supported by: Lecturer Md. Nahid Hasan & Dept. of CSE, DIU  

---

## 🤝 Get in Touch

For questions, feedback, or collaboration, please open an issue, or reach out at `monirbishal1@gmail.com`.

---

## ✅ Contribution

Contributions are welcome! Please fork the repo, make your changes, and submit a pull request.

---

Thank you for checking out **Dibhashi**! We hope it helps foster more accessible Bangla-language video content. 😊
