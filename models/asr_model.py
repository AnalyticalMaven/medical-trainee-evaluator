from transformers import pipeline
import torch

# Initialize the ASR pipeline with explicit dtype
asr_pipeline = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    torch_dtype=torch.float32  # Explicitly set dtype
)

def transcribe_audio(audio_file):
    """Convert speech to text"""
    try:
        result = asr_pipeline(audio_file)
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return "Transcription failed"