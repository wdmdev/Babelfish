import os
import itertools
from tqdm import tqdm

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "ESD")
DATA_DIR = os.path.join(os.path.dirname(__file__), "Emotional Speech Dataset (ESD)")

def key_func(name:str):
    id = int(name.split('_')[-1].split('.')[0])
    return id

def create_list(list_type:str):
    print(f'Creating {list_type} list of mappings for emotional speech conversion...')
    speech_mappings = []

    current_speaker_id = 0

    for speaker in tqdm(os.listdir(DATA_DIR)):
        speaker_path = os.path.join(DATA_DIR, speaker)

        angry_path = os.path.join(speaker_path, 'Angry', list_type)     
        happy_path = os.path.join(speaker_path, 'Happy', list_type)     
        neutral_path = os.path.join(speaker_path, 'Neutral', list_type)     
        sad_path = os.path.join(speaker_path, 'Sad', list_type)     
        suprised_path = os.path.join(speaker_path, 'Surprise', list_type)     

        angry_speech = sorted(os.listdir(angry_path), key=key_func)
        happy_speech = sorted(os.listdir(happy_path), key=key_func)
        neutral_speech = sorted(os.listdir(neutral_path), key=key_func)
        sad_speech = sorted(os.listdir(sad_path), key=key_func)
        suprised_speech = sorted(os.listdir(suprised_path), key=key_func)

        for i in range(len(angry_speech)):
            speaker_map = []
            speaker_map.append('|'.join([os.path.join(angry_path, angry_speech[i]), str(current_speaker_id)]))
            speaker_map.append('|'.join([os.path.join(happy_path, happy_speech[i]), str(current_speaker_id)]))
            speaker_map.append('|'.join([os.path.join(neutral_path, neutral_speech[i]), str(current_speaker_id)]))
            speaker_map.append('|'.join([os.path.join(sad_path, sad_speech[i]), str(current_speaker_id)]))
            speaker_map.append('|'.join([os.path.join(suprised_path, suprised_speech[i]), str(current_speaker_id)]))
            speech_mappings.extend(speaker_map)
            current_speaker_id += 1

        #TODO Make code create new folder structure with each speaker mapping as a new person

    
    with open(os.path.join(os.path.dirname(__file__), f'esd_{list_type}_list.txt'), 'w') as mapping_list:
        mapping_list.write('\n'.join(speech_mappings))
            

if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        create_list('train') 
        create_list('evaluation')