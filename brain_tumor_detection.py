import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets
from torchvision.transforms import v2
from torch.utils.data import DataLoader

# Definícia rozmerov obrázka
IMG_SIZE = (224, 224)
BATCH_SIZE = 32


train_transforms = v2.Compose([
    v2.Resize(IMG_SIZE),
    v2.RandomHorizontalFlip(p=0.5),      
    v2.RandomRotation(degrees=(-15, 15)),        
    v2.ColorJitter(brightness=0.2, contrast=0.2), 
    v2.ToImage(),                         
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) 
])


val_transforms = v2.Compose([
    v2.Resize(IMG_SIZE),
    v2.ToImage(),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


train_dataset = datasets.ImageFolder(
    root='/Users/macbook/Documents/GitHub/Anteater/tumor_dataset/Training', 
    transform=train_transforms
)
val_dataset = datasets.ImageFolder(
    root='/Users/macbook/Documents/GitHub/Anteater/tumor_dataset/Testing', 
    transform=val_transforms
)



train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, pin_memory=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0, pin_memory=True)

