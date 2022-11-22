import os
import torch
import librosa
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# load model and tokenizer
processor = Wav2Vec2Processor.from_pretrained(
    "chcaa/xls-r-300m-danish-nst-cv9")
model = Wav2Vec2ForCTC.from_pretrained(
    "chcaa/xls-r-300m-danish-nst-cv9")

sampling_rate = 16000
path = os.path.join(os.path.dirname(__file__), 'common_voice_da_27769309.wav')
wave, sr = librosa.load(path, sr=sampling_rate)

# tokenize
input_values = processor(wave, return_tensors="pt", padding="longest", sampling_rate=sampling_rate).input_values  # Batch size 1

# retrieve logits
logits = model(input_values).logits

# take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)
print(' '.join(transcription))