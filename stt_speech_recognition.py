import tkinter as tk
from tkinter import filedialog, Label, Button, Text
import speech_recognition as sr
import torch
import librosa
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

# Load Wav2Vec2 model
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

# Function to use Google Speech Recognition
def transcribe_google(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Could not understand the audio."
        except sr.RequestError:
            return "Error connecting to Google API."

# Function to use Wav2Vec2 for offline transcription
def transcribe_wav2vec(audio_path):
    audio, sr = librosa.load(audio_path, sr=16000)
    input_values = processor(audio, return_tensors="pt", sampling_rate=16000).input_values
    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    return processor.batch_decode(predicted_ids)[0]

# Function to handle file selection and transcription
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.flac")])
    if file_path:
        text_box.delete("1.0", tk.END)  # Clear previous text
        text_box.insert(tk.END, "Transcribing...\n")
        root.update()
        
        # Choose transcription method
        if method_var.get() == "Google API":
            transcription = transcribe_google(file_path)
        else:
            transcription = transcribe_wav2vec(file_path)
        
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, transcription)

# Create the GUI
root = tk.Tk()
root.title("Speech-to-Text Application")
root.geometry("600x400")

Label(root, text="Choose an audio file to transcribe:", font=("Arial", 12)).pack(pady=10)

method_var = tk.StringVar(value="Google API")
google_radio = tk.Radiobutton(root, text="Google API (Online)", variable=method_var, value="Google API")
wav2vec_radio = tk.Radiobutton(root, text="Wav2Vec2 (Offline)", variable=method_var, value="Wav2Vec2")
google_radio.pack()
wav2vec_radio.pack()

Button(root, text="Select File", command=select_file, font=("Arial", 12)).pack(pady=10)

text_box = Text(root, height=10, wrap="word", font=("Arial", 12))
text_box.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
