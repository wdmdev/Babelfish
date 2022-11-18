import os
import shutil
import itertools
from tqdm import tqdm

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "ESD")
TARGET_EMOTIONS = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
DATA_DIR = os.path.join(os.path.dirname(__file__), "Emotional Speech Dataset (ESD)")

def create_list(list_type:str):
    print(f'Creating {list_type} list of mappings for emotional speech conversion...')
    speech_mappings = []

    for emotion_id, emotion in enumerate(tqdm(TARGET_EMOTIONS)):
        for speaker in os.listdir(DATA_DIR):
            speaker_path = os.path.join(DATA_DIR, speaker)
            emotion_path = os.path.join(speaker_path, emotion, list_type)
            emotion_output = os.path.join(OUTPUT_DIR, emotion)   

            for emotion_speech in os.listdir(emotion_path):
                emotion_speech_path = os.path.join(emotion_path, emotion_speech)
                emotion_out_path = os.path.join(emotion_output, emotion_speech)
                shutil.copy(emotion_speech_path, emotion_out_path)

                speech_mappings.append('|'.join([emotion_out_path, str(emotion_id)]))
    
    
    with open(os.path.join(os.path.dirname(__file__), f'esd_{list_type}_list.txt'), 'w') as mapping_list:
        mapping_list.write('\n'.join(speech_mappings))
            

if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        for emotion in TARGET_EMOTIONS:
            os.mkdir(os.path.join(OUTPUT_DIR, emotion))

        create_list('train') 
        create_list('evaluation')