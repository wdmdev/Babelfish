import os
import random
from tqdm import tqdm

DATA_DIR = os.path.join(os.path.dirname(__file__), "Babelfish_Split_Multi")

def create_lists():
    print(f'Creating train and validation lists of mappings for babelfish...')
    validation_mappings = []
    train_mappings = []
    
    for speaker_id, speaker in enumerate(tqdm(os.listdir(DATA_DIR))):
        speaker_path = os.path.join(DATA_DIR, speaker)
        if os.path.isdir(speaker_path):

            speaker_files = os.listdir(speaker_path)

            #validation
            for speaker_file in speaker_files[:100]:
                file_path = os.path.join(speaker_path, speaker_file)
                validation_mappings.append('|'.join([file_path, str(speaker_id)]))

            #Train
            for speaker_file in speaker_files[100:]:
                file_path = os.path.join(speaker_path, speaker_file)
                train_mappings.append('|'.join([file_path, str(speaker_id)]))
    
    #Validation list
    with open(os.path.join(os.path.dirname(__file__), f'babelfish_split_multi_validation_list.txt'), 'w') as validation_mapping_list:
        random.shuffle(validation_mappings)
        validation_mapping_list.write('\n'.join(validation_mappings))

    #Train list
    with open(os.path.join(os.path.dirname(__file__), f'babelfish_split_multi_train_list.txt'), 'w') as train_mapping_list:
        random.shuffle(train_mappings)
        train_mapping_list.write('\n'.join(train_mappings))
            

if __name__ == '__main__':
    if os.path.exists(DATA_DIR):
        create_lists() 