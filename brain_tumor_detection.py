import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets
from torchvision.transforms import v2
from torch.utils.data import DataLoader

# Definícia rozmerov obrázka
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# 1. Augmentácia pre trénovacie dáta (vnáša šum a variabilitu)
train_transforms = v2.Compose([
    v2.Resize(IMG_SIZE),
    v2.RandomHorizontalFlip(p=0.5),      # Náhodné prevrátenie horizontálne
    v2.RandomRotation(degrees=(-15, 15)),        # Náhodné otočenie o max 15 stupňov
    v2.ColorJitter(brightness=0.2, contrast=0.2), # Jemná úprava jasu a kontrastu
    v2.ToImage(),                         # Konverzia na Tensor typu uint8
    v2.ToDtype(torch.float32, scale=True),# Pretypovanie na float32 a škálovanie 0 až 1
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # ImageNet normalizácia
])

# 2. Transformácia pre validačné/testovacie dáta (žiadna augmentácia, len úprava formátu)
val_transforms = v2.Compose([
    v2.Resize(IMG_SIZE),
    v2.ToImage(),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 3. Načítanie z priečinkov (predpokladá štruktúru: data/train/klasa1, data/train/klasa2...)
# 3. Načítanie z hlavných priečinkov (ImageFolder sám prečíta podpriečinky vo vnútri)
train_dataset = datasets.ImageFolder(
    root='/Users/macbook/Documents/GitHub/Anteater/tumor_dataset/Training', 
    transform=train_transforms
)
val_dataset = datasets.ImageFolder(
    root='/Users/macbook/Documents/GitHub/Anteater/tumor_dataset/Testing', 
    transform=val_transforms
)


# 4. DataLoader zabezpečí dávkovanie (batching), miešanie (shuffle) a paralelné načítanie (num_workers)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, pin_memory=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0, pin_memory=True)

print("Pripravujem načítanie dát...")

try:
    # 1. Skontrolujeme, či PyTorch vidí triedy
    print(f"Nájdené podtriedy (priečinky): {train_dataset.classes}")

    # 2. Vynútime načítanie úplne prvej dávky obrázkov
    images, labels = next(iter(train_loader))

    # 3. Ak kód dôjde sem, všetko funguje
    print("\n🎉 ÚSPECH! Obrázky boli úspešne spracované a načítané.")
    print(f"Počet obrázkov v jednej dávke: {images.shape[0]}")
    print(f"Rozmery obrázkov (Kanály, Výška, Šírka): {images.shape[1:]}")
except Exception as e:
    print("\n❌ Nastala chyba pri načítaní dát:")
    print(e)