import os
import itertools
from tqdm import tqdm

DATA_DIR = os.path.join(os.path.dirname(__file__), "Emotional Speech Dataset (ESD)")

def key_func(name:str):
    id = int(name.split('_')[-1].split('.')[0])
    return id

def create_list(list_type:str):
    print(f'Creating {list_type} list of mappings for emotional speech conversion...')
    speech_mappings = []

    for speaker in tqdm(os.listdir(DATA_DIR)):
        speaker_path = os.path.join(DATA_DIR, speaker)

        angry_path = os.path.join(speaker_path, 'Angry', list_type)     
        happy_path = os.path.join(speaker_path, 'Happy', list_type)     
        neutral_path = os.path.join(speaker_path, 'Neutral', list_type)     
        sad_path = os.path.join(speaker_path, 'Sad', list_type)     
        suprised_path = os.path.join(speaker_path, 'Surprise', list_type)     

        emotion_paths = [angry_path, happy_path, neutral_path, sad_path, suprised_path]
        emotion_path_combinations = list(itertools.product(emotion_paths,emotion_paths))

        for emotion1_path,emotion2_path in emotion_path_combinations:
            emotion1_speech_files = sorted(os.listdir(emotion1_path), key=key_func)
            emotion2_speech_files = sorted(os.listdir(emotion2_path), key=key_func)

            emotion_mappings = ['|'.join([os.path.join(emotion1_path, e1),os.path.join(emotion2_path,e2)]) 
                                for e1,e2 in zip(emotion1_speech_files, emotion2_speech_files)]
            speech_mappings.extend(emotion_mappings)
    
    with open(os.path.join(os.path.dirname(__file__), f'esd_{list_type}_list.txt'), 'w') as mapping_list:
        mapping_list.write('\n'.join(speech_mappings))
            

if __name__ == '__main__':
    create_list('train') 
    create_list('evaluation')