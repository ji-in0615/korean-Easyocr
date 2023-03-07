# korean-EasyOCR

This code is based on EasyOCR.
I tried to fine tune with training data that I generated myself.
It is used only for korean OCR.

## EasyOCR
EasyOCR is a python module for extracting text from image. It is a general OCR that can read both natural scene text and dense text in document. We are currently supporting 80+ languages and expanding.

## Reauirements
### Process & ref
- generate training data : [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator)
- convert training data : [TRDG2DTRB](https://github.com/DaveLogs/TRDG2DTRB)
- training model  : [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark)
- use model : [EasyOCR](https://github.com/JaidedAI/EasyOCR)
