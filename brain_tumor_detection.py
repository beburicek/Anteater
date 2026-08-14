
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

DATASET_PATH = '/Users/macbook/Documents/GitHub/Anteater/tumor_dataset/Testing/glioma'
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32



data_transforms = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)), 
    transforms.RandomHorizontalFlip(p=0.5),      
    transforms.ToTensor(),                       
    transforms.Normalize(                        
        mean=[0.485, 0.456, 0.406], 
        std=[0.229, 0.224, 0.225]
    )
])