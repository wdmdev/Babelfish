import os
import shutil
import itertools
from tqdm import tqdm

DATA_DIR = os.path.join(os.path.dirname(__file__), "Babelfish")

def create_list(list_type:str):
    print(f'Creating {list_type} list of mappings for babelfish...')
    speech_mappings = []
    speakers = {s_id: s for s_id, s in enumerate(os.listdir(DATA_DIR)) if s != 'synthetic'}

    for synthetic_file in os.listdir(os.path.join(DATA_DIR, 'synthetic', list_type)):
        for speaker_id, speaker in speakers.items():
            speaker_path = os.path.join(DATA_DIR, speaker, list_type)

            for speaker_file in os.listdir(speaker_path):
                file_path = os.path.join(speaker_path, speaker_file)
                speech_mappings.append('|'.join([file_path, str(speaker_id)]))
                speech_mappings.append('|'.join([file_path, str(speaker_id)]))
    
    
    with open(os.path.join(os.path.dirname(__file__), f'babelfish_{list_type}_list.txt'), 'w') as mapping_list:
        mapping_list.write('\n'.join(speech_mappings))
            

if __name__ == '__main__':
    if os.path.exists(DATA_DIR):
        create_list('train') 
        create_list('validation')