# SPEECH-RECOGNITION-SYSTEM

SUMMARY:
With the help of the GUI-based Speech-to-Text Application, users may convert spoken words into text by uploading an audio file from their local device. It offers two transcribing techniques:
Internet connectivity is required for the online Google SpeechRecognition API function.
Wav2Vec2 (Offline technique utilizing the Wav2Vec 2.0 model from Hugging Face)
For jobs like transcribing meetings, seminars, interviews, and any other speech-based material, this tool is helpful.

FEATURES:
>>User-Friendly GUI: Built using Tkinter for a simple and interactive interface.
>>Multiple Transcription Methods:
Google API (Online): Uses SpeechRecognition to transcribe audio files.
Wav2Vec2 (Offline): Uses a pre-trained deep learning model to transcribe speech without requiring an internet connection.
>>Supports Multiple Audio Formats: Accepts .wav, .mp3, and .flac files.
>>Fast and Accurate Transcriptions: Uses powerful pre-trained models for speech recognition.

INSTALLATION:
Prerequisites:
Ensure you have Python (>=3.7) installed on your system.
Step 1: Clone the Repository:
>>git clone https://github.com/your-username/speech-to-text-app.git
>>cd speech-to-text-app
Step 2: Install Dependencies
Run the following command to install the required Python libraries:
>>pip install SpeechRecognition pydub transformers torch librosa tkinterfiledialog

USAGE:
Running the Application:
Run the Python script to launch the application:
>>python speech_to_text_app.py

HOW TO USE:
1.Launch the application.
2.Choose the transcription method:
Google API (Online)
Wav2Vec2 (Offline)
3.Select an audio file (.wav, .mp3, or .flac).
4.Wait for transcription to be processed and displayed in the text box.
5.Copy the transcribed text for further use.

TECHNOLOGY STACK:
-Python: Core programming language.
-Tkinter: GUI framework for building the interface.
-SpeechRecognition: For online speech-to-text conversion using Google's API.
-Transformers & Torch: Used for offline transcription with Wav2Vec2.
-Librosa: Handles audio file processing.

TROUBLESHOOTING:
1. Google API Not Working?
Ensure you have an active internet connection.
Try using the Wav2Vec2 (Offline) method instead.

2. Audio File Not Recognized?
Ensure your file format is .wav, .mp3, or .flac.
Convert the file to .wav using an online tool if needed.

3. Model Download Takes Time?
The Wav2Vec2 model is large (~1GB). The first run may take time to download.

FUTURE IMPROVEMENTS:
-Add support for more languages.
-Implement real-time speech-to-text.
-Optimize performance for longer recordings.
-Add export options for saving transcriptions.

CONCLUSION:
The Speech-to-Text Application is a powerful and accessible tool for converting spoken words into text with ease. With its user-friendly GUI and the ability to choose between online and offline transcription methods, it serves as a versatile solution for various transcription needs. Whether you are transcribing meetings, lectures, or personal notes, this application provides a seamless and efficient experience. Future enhancements will further improve its accuracy and usability, making it even more valuable for users worldwide.

OUTPUT:

![Image](https://github.com/user-attachments/assets/9f807092-1963-4322-9862-6984f4274440)

![Image](https://github.com/user-attachments/assets/08e99b8f-f01b-4cfb-92d8-3c1b4ff1b368)

![Image](https://github.com/user-attachments/assets/0eb9ce48-aacf-4cf0-824c-19b515ad220e)
