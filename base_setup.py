import os
import zipfile
import gdown
import shutil

SPEAKERS = ['p225', 'p226', 'p227', 'p228', 'p229', 'p230', 'p231', 'p232', 'p233', 'p236', 'p239',
            'p240', 'p243', 'p244', 'p254', 'p256', 'p258', 'p259', 'p270', 'p273'] 

DATA_PATH = os.path.join(os.path.dirname(__file__), 'Data')
VOCODER_PATH = os.path.join(os.path.dirname(__file__))


def is_valid_data():

    if os.path.exists(DATA_PATH):
        data_items = os.listdir(DATA_PATH)
        if all([s in data_items for s in SPEAKERS]):
            return True
    
    return False

def download_data(url):

    data_zip_path = os.path.join(DATA_PATH, 'data.zip')

    gdown.download(url, data_zip_path, quiet=False)

    with zipfile.ZipFile(data_zip_path, 'r') as zip:
        zip.extractall(DATA_PATH)
    
    os.remove(data_zip_path)

    unzipped_data_folder = os.path.join(DATA_PATH, 'Data')
    for f in os.listdir(unzipped_data_folder): 
        shutil.move(os.path.join(DATA_PATH, 'Data', f), os.path.join(DATA_PATH, f))

    os.rmdir(unzipped_data_folder)

def download_vocoder(url):
    vocoder_zip_path = os.path.join(os.path.dirname(__file__), 'Vocoder.zip')

    gdown.download(url, vocoder_zip_path, quiet=False)

    with zipfile.ZipFile(vocoder_zip_path, 'r') as zip:
        zip.extractall(VOCODER_PATH)
    
    os.remove(vocoder_zip_path)

if __name__ == '__main__':

    # Data download made by the authors of the StarGANv2-VC paper
    data_url = 'https://drive.google.com/uc?id=1t7QQbu4YC_P1mv9puA_KgSomSFDsSzD6'
    vocoder_url = 'https://drive.google.com/uc?id=1q8oSAzwkqi99oOGXDZyLypCiz0Qzn3Ab'

    if not is_valid_data():
        print('Missing valid data for this setup')
        print('Downloading data...')
        download_data(data_url)
    
    if not os.path.exists(os.path.join(VOCODER_PATH, 'Vocoder')):
        print('Missing vocoder')
        print('Downloading vocoder...')
        download_vocoder(vocoder_url)

    print('Setup completed!')