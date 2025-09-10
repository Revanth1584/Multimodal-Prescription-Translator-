import gradio as gr
from deep_translator import GoogleTranslator
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

# Language mapping
lang_map = {
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Malayalam": "ml"
}

def process_audio(audio_path, target_lang_full):
    audio_text = "[No audio uploaded]"

    # 1️⃣ Audio transcription
    try:
        if audio_path:
            # Convert audio to WAV (compatible format)
            wav_path = tempfile.mktemp(suffix=".wav")
            AudioSegment.from_file(audio_path).export(wav_path, format="wav")

            recognizer = sr.Recognizer()
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                audio_text = recognizer.recognize_google(audio_data)
    except Exception as e:
        audio_text = f"Audio transcription error: {str(e)}"

    # 2️⃣ Translate
    target_lang_code = lang_map.get(target_lang_full, "hi")
    try:
        translated_text = GoogleTranslator(source="auto", target=target_lang_code).translate(audio_text)
    except Exception as e:
        translated_text = f"Translation error: {str(e)}"

    return audio_text, translated_text

# Gradio Interface
demo = gr.Interface(
    fn=process_audio,
    inputs=[
        gr.Audio(type="filepath", label="Upload Patient Audio"),
        gr.Dropdown(list(lang_map.keys()), label="Target Language", value="Hindi"),
    ],
    outputs=[
        gr.Textbox(label="Transcribed Audio"),
        gr.Textbox(label="Translated Audio"),
    ],
    title="Audio Medical Translation System",
    description="Upload patient audio. Transcription and translation will appear below."
)

if __name__ == "__main__":
    demo.launch()

