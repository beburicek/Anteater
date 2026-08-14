
import pandas as pd
import tf_keras as keras
from tf_keras.models import Sequential
from tf_keras import layers, models

DATASET_PATH = '/Users/macbook/Documents/GitHub/Anteater/tumor_dataset'
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32