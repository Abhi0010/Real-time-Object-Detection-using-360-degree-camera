import torch

class Yolov5:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', device='cpu' , pretrained=True)
        
    def predict(self, image):
        return self.model(image)
