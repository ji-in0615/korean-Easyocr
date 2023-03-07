import torch

state_dict = torch.load('/data/IMT/ocr_ko/pre_trained_model/korean_g2.pth', map_location='cpu')
torch.save(state_dict, '/data/IMT/ocr_ko/pre_trained_model/korean_g2.pth', _use_new_zipfile_serialization=False)
# data = torch.load('/data/IMT/ocr_ko/pre_trained_model/korean_g2.pth')
# torch.save(data.type(torch.float32),'/data/IMT/ocr_ko/pre_trained_model/korean_g2_test.pt')
# data = torch.load('/data/IMT/ocr_ko/pre_trained_model/korean_g2_test.pt')  