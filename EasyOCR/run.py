from easyocr.easyocr import *
import easyocr
import json
from numpyencoder import NumpyEncoder

# GPU 설정
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2,3'


def get_files(path):
    file_list = []

    files = [f for f in os.listdir(path) if not f.startswith('.')]  # skip hidden file
    files.sort()
    abspath = os.path.abspath(path)
    for file in files:
        file_path = os.path.join(abspath, file)
        file_list.append(file_path)

    return file_list, len(file_list)


if __name__ == '__main__':

    # Using default model
    # reader = easyocr.Reader(['ko'], gpu=True)

    # Using custom model
    reader = Reader(['ko'], gpu=True,
                    model_storage_directory='/data/IMT/ocr_ko/user_network/data+font/',
                    user_network_directory='/data/IMT/ocr_ko/user_network/data+font/',
                    recog_network='custom')

    files, count = get_files("/data/IMT/ocr_ko/test_set/Their_circumstances/1/")
    
    file_path = "./EasyOCR/"

    for idx, file in enumerate(files):
        filename = os.path.basename(file)

        result = reader.readtext(file)

        # ./easyocr/utils.py 733 lines
        # result[0]: bbox
        # result[1]: string
        # result[2]: confidence
        for (bbox, string, confidence) in result:
            print("filename: '%s', confidence: %.4f, string: '%s'" % (filename, confidence, string))
            print('bbox: ', bbox)
            
            
            with open('result.json', 'w') as file_path:
                for (filename, confidence, string, bbox) in result:
                    json.dump(result, file_path, indent=4, ensure_ascii=False, cls=NumpyEncoder)

