import os
import torch
import torchaudio
from tqdm import tqdm
from speechbrain.pretrained import SpectralMaskEnhancement

DATA_DIR = os.path.join(os.path.dirname(__file__), "Denoised Babelfish")
MODEL = SpectralMaskEnhancement.from_hparams(
    source="speechbrain/metricgan-plus-voicebank",
    savedir="pretrained_models/metricgan-plus-voicebank",
)

def denoise_file(file_path):
    # Load and add fake batch dimension
    noisy = MODEL.load_audio(file_path).unsqueeze(0)
    # Add relative length tensor
    enhanced = MODEL.enhance_batch(noisy, lengths=torch.tensor([1.]))
    os.remove(file_path)
    torchaudio.save(file_path, enhanced.cpu(), 16000)

def create_list(list_type:str):
    print(f'Creating {list_type} list of mappings for babelfish...')
    speech_mappings = []
    speakers = os.listdir(DATA_DIR)
    speaker_len = len(speakers)
    
    for speaker_id, speaker in enumerate(speakers):
        print(f'Denoising {list_type} files for speaker {speaker_id+1}/{speaker_len}')

        speaker_path = os.path.join(DATA_DIR, speaker, list_type)
        for speaker_file in tqdm(os.listdir(speaker_path)):
            file_path = os.path.join(speaker_path, speaker_file)
            denoise_file(file_path)
            speech_mappings.append('|'.join([file_path, str(speaker_id)]))
    
    with open(os.path.join(os.path.dirname(__file__), f'denoised_babelfish_{list_type}_list.txt'), 'w') as mapping_list:
        mapping_list.write('\n'.join(speech_mappings))
            

if __name__ == '__main__':
    if os.path.exists(DATA_DIR):
        create_list('train') 
        create_list('validation')