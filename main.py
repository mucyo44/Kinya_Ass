import os
import time
import torch
import torchaudio
import sounddevice as sd
import wavio
import pyttsx3
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Initialize TTS
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

# Load model
model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")
processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")

# Q&A dictionary
qa_dict = {
    "amakuru": "Ni meza cyane, urakoze kubaza!",
    "witwa": "Nitwa KinyaVoice Assistant.",
    "urakoze": "Nawe urakoze cyane!",
    "amakuru yawe": "Ni meza cyane!",
    "ukora iki": "Ndi umufasha mu kuvugana no gusubiza ibibazo byawe.",
}

# Settings
duration = 5  # seconds
sample_rate = 16000
output_dir = "audio"
os.makedirs(output_dir, exist_ok=True)

def record_audio(filename):
    print("🎙️ Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, audio_data, sample_rate, sampwidth=2)
    print(f"✅ Saved recording to {filename}")

def transcribe_audio(filename):
    try:
        # Check backend
        waveform, sr = torchaudio.load(filename)
        inputs = processor(waveform.squeeze(), sampling_rate=sr, return_tensors="pt")
        with torch.no_grad():
            predicted_ids = model.generate(inputs["input_features"])
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        return transcription.lower()
    except Exception as e:
        print("❌ Transcription error:", str(e))
        return None  # indicate transcription failure

def get_answer(transcription):
    if transcription is None:
        return "Subiramo neza."
    for key in qa_dict:
        if key in transcription:
            return qa_dict[key]
    return "Ntabyo nzi."

def speak(text):
    print("🗣️ Speaking...")
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    print("👂 Voice Assistant irategereje ikibazo...")
    while True:
        filename = os.path.join(output_dir, f"question_{int(time.time())}.wav")
        record_audio(filename)
        transcription = transcribe_audio(filename)

        if transcription:
            print("🗣️ Wavuze:", transcription)
        else:
            print("🗣️ Wavuze: [Ntibyumvikanye neza]")

        response = get_answer(transcription)
        print("🤖 Ibisubizo:", response)
        speak(response)

        again = input("\n🎤 Ushaka kongera kubaza? (y/n): ").strip().lower()
        if again != 'y':
            speak("Murakoze gukoresha KinyaVoice Assistant. Murabeho!")
            print("👋 Murakoze gukoresha KinyaVoice Assistant!")
            break

if __name__ == "__main__":
    main()
