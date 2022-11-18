import os
import shutil
import zipfile
import gdown
import shutil

SPEAKERS = ['0011', '0012', '0013', '0014', '0015', '0016', '0017', '0018', '0019', '0020'] 

DATA_PATH = os.path.join(os.path.dirname(__file__), 'Data')
VOCODER_PATH = os.path.join(os.path.dirname(__file__))


def is_valid_data():
    if os.path.exists(DATA_PATH):
        data_items = os.listdir(DATA_PATH)
        if all([s in data_items for s in SPEAKERS]):
            return True
    
    return False

def download_data(url):
    data_zip_path = os.path.join(DATA_PATH, 'Emotional Speech Dataset (ESD).zip')

    gdown.download(url, data_zip_path, quiet=False)

    with zipfile.ZipFile(data_zip_path, 'r') as zip:
        zip.extractall(DATA_PATH)

    os.remove(data_zip_path)

    # Only speaker 0011 to 0020 are English speakers
    # We remove the rest
    unzipped_data_path = os.path.join(DATA_PATH, 'Emotional Speech Dataset (ESD)') 
    for f in os.listdir(unzipped_data_path):
        if not f in SPEAKERS:
            shutil.rmtree(os.path.join(unzipped_data_path, f))



def download_vocoder(url):
    vocoder_zip_path = os.path.join(os.path.dirname(__file__), 'Vocoder.zip')

    gdown.download(url, vocoder_zip_path, quiet=False)

    with zipfile.ZipFile(vocoder_zip_path, 'r') as zip:
        zip.extractall(VOCODER_PATH)
    
    os.remove(vocoder_zip_path)

if __name__ == '__main__':

    # Data download made by the authors of the StarGANv2-VC paper
    data_url = 'https://drive.google.com/uc?id=1scuFwqh8s7KIYAfZW1Eu6088ZAK2SI-v'
    vocoder_url = 'https://drive.google.com/uc?id=1q8oSAzwkqi99oOGXDZyLypCiz0Qzn3Ab'

    if not is_valid_data():
        print('Missing valid emotional speech data for this setup')
        print('Downloading data...')
        download_data(data_url)
    
    if not os.path.exists(os.path.join(VOCODER_PATH, 'Vocoder')):
        print('Missing vocoder')
        print('Downloading vocoder...')
        download_vocoder(vocoder_url)

    print('Setup completed!')