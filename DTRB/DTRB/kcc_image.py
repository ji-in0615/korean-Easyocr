from trdg.generators import (
    GeneratorFromStrings,
)

import glob
import re
import pickle
from tqdm import tqdm

with open("list.pickle","rb") as f:
    dict_ex = pickle.load(f)

ocr_strings = list(dict_ex)

font_path = '/home/ubuntu/workspace/230213_easyocrf_jiin/TRDG/trdg/fonts/*'
font_list = glob.glob(font_path)
font_list_path = [file for file in font_list if file.endswith(".ttf")]

generator = GeneratorFromStrings(
    ocr_strings,
    count=len(ocr_strings),
    random_blur=True,
    background_type=3,
    image_dir='./image',
    fonts=font_list_path,
    # text_color='#FFFFFF',
    text_color='#000000',
    size=40    #40 ~ 50, random.randint(50,80)
)

print(len(ocr_strings), "이미지 생성")

f = open("./gt.txt", 'a+', encoding='utf-8')

import datetime
str_datetime = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%dH%M%S')
index = 0

start_index = 0

for img, lbl in tqdm(generator, total=len(ocr_strings)):
    # Do something with the pillow images here
    if index  >= start_index:
        img.save("./test/{0}_{1:010d}.jpg".format(str_datetime, index), format='JPEG')
        f.write("./test/{0}_{1:010d}.jpg\t{2}\n".format(str_datetime, index, re.sub('[\/:*?"<>|]','',lbl)))
    index += 1


f.close()