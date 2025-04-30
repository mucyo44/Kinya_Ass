# 🗣️ Kinyarwanda Voice Assistant – "KinyaWhisper"

A voice-enabled mini assistant that understands **Kinyarwanda** and responds , designed to simulate how intelligent humanoid robots interact with humans in local languages. Built from scratch using ASR (Whisper), NLP, and TTS (pyttsx3), this project showcases the potential of AI for localized voice interaction.

---

## 🎯 Project Summary

This project was developed as part of an **Intelligent Robotics** assignment to build a simple voice assistant for Kinyarwanda speakers. It includes:

- 🎤 **Automatic Speech Recognition (ASR)**: Fine-tuned Whisper model on a custom Kinyarwanda dataset.
- 🧠 **Natural Language Processing (NLP)**: Rule-based question-answer matching with fuzzy logic.
- 🗣️ **Text-to-Speech (TTS)**: Voice responses using the `pyttsx3` library.

---

## 📁 Folder Structure

```
.
├── audio/                   # 44 custom audio samples (Kinyarwanda)
├── dataset.jsonl           # Metadata: audio path + transcription
├── kinya-whisper-model/    # Fine-tuned Whisper model output
├── train.py                # Whisper training script
├── inference.py            # Batch transcription script
├── main.py                 # Batch voice assistant (NLP + TTS)
├── bach_main.py            # CLI: record + respond to live audio
├── transcriptions.txt      # Output transcriptions
├── README.md               # Project documentation
```

---

## 🚀 How It Works

1. **ASR**: User speaks or loads audio → Whisper model transcribes it.
2. **NLP**: Assistant uses exact/fuzzy matching to map transcription to predefined answers.
3. **TTS**: Assistant speaks the matched answer aloud.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **OpenAI Whisper (fine-tuned)**
- **Transformers (Hugging Face)**
- **Torchaudio**
- **Pyttsx3** (offline TTS)
- **Difflib** for fuzzy matching
- **Sounddevice** for live mic input (CLI mode)

---

## 🧠 Training Details

- Dataset: 44-word Kinyarwanda dataset built using [BearAudioTool](https://www.bearaudiotool.com/)
- Model: Fine-tuned `openai/whisper-small`
- Epochs:
  - 1st run: 40 epochs
  - 2nd run over pre fine-tuned 40 epochs model : 20 more epochs
  - 3rd run over pre fine-tuned 40+20 epochs model: 10 final epochs
- Inference tested on all 44 samples with good to generous transcription accuracy

---

## ▶ How To Run

### 1. Clone and Install Requirements

```bash
git clone https://github.com/mucyo44/kinya_Ass.git
cd kinyawhisper-voice-assistant
pip install transformers[torch] datasets torchaudio warnings difflib pyttsx3 sounddevice
```
### 2. Run Main App (Batch Mode)

```bash
python main.py
```

Transcribes all WAV files in `audio/`, matches them to answers, and reads them aloud.

### 3. Run CLI App (Live Recording)

- uncomment line 66 on  the initial run

```python
# model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small") #first time
```
- comment the line following 66 on the initial un

```python
model = WhisperForConditionalGeneration.from_pretrained("./kinya-whisper-model")
```

```bash
python bach_main.py
```

Records a live voice input from your mic, transcribes it, matches it, and responds via voice.

### 4. Run ASR Inference Script Only

```bash
python inference.py
```

Generates text transcriptions only (no NLP or TTS).

### 5. Train Your Own Model (Optional)

```bash
python train.py
```

Fine-tunes Whisper using `dataset.jsonl` and saves to `./kinya-whisper-model/`.

---

## 📌 Sample QA Dictionary

| Question (Kinyarwanda)        | Assistant Response                         |
|------------------------------|--------------------------------------------|
| `amakuru yawe`               | `Ni meza, urakoze! nkufashe iki?`          |
| `witwa nde`                  | `Nitwa Mudasa AI.`                         |
| `uzi ikinyarwanda`           | `Nkunda gufasha abantu mu rurimi rwacu.`  |
| `wiriwe`                     | `wiriwe neza`                              |
| `umworozi ni iki`            | `umworozi ni umuntu utunga amatungo`      |

Fuzzy and partial matches are supported to improve recognition.

---

## 🧪 Example Audio Commands

Upload your own `.wav` files into the `audio/` folder or record with `bach_main.py`. Examples:
- `muraho`
- `inzovu`
- `umwana`
- `vuga gahoro`
- `kwandika`

---

## 🎓 Academic Info

- **Course**: Intelligent Robotics  
- **Instructor**: [Gabriel Baziramwabo ] 
- **School**: [Rwanda Coding Academy](https://rca.ac.rw/)  

---

## 👤 Author

**MUCYO Honorine**  
Email: honorinemucyo4b@gmail.com 

