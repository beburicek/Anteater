import kagglehub
import pandas as pd

path = kagglehub.dataset_download("masoudnickparvar/brain-tumor-mri-dataset")

print("Path to dataset files:", path)
df=pd.read_csv(path + "/data.csv")
print(df.head())

