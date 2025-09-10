# 🩺 Multimodal Prescription Translator

Automatically transcribe patient audio and translate it into multiple languages for easier medical understanding.  

---

## 📸 Overview

Doctors and healthcare professionals often give verbal instructions or write short notes in prescriptions. Understanding them can be challenging for patients. This app:

- Transcribes patient audio 🎤
- Translates the extracted text 🌐
- Provides a simple interface for quick results 🖥️  

---

## 🚀 Live Demo

Try it live (mobile-friendly) 👉 [Multimodal Prescription Translator](https://revanthkaushik-multimodal-prescription-translate.hf.space/?__theme=dark&deep_link=izwRpCP-cIc)

**How to use:**

1. Upload a patient audio file 🎧  
2. Select target language 🌎  
3. Get instant transcription and translation ✨  

---

## 🛠️ Tech Stack

- **Python** – Core logic and processing 🐍  
- **Gradio** – Interactive web UI 🎨  
- **SpeechRecognition & pydub** – Audio transcription 🎤  
- **deep-translator** – Multilingual translation 🌐  
- **Hugging Face Spaces** – Free hosting & deployment 🚀  

---

## 🧠 How It Works

1. Upload an audio file 🎧  
2. The app converts it to a compatible format (`wav`)  
3. Audio is transcribed to text using **SpeechRecognition**  
4. Transcribed text is sent to **GoogleTranslator** for target language translation  
5. Results are displayed in two boxes:
   - Extracted text 🔹  
   - Translated text 🔹  

---

## 📁 Project Structure

