import requests
import zipfile
import os

# 1. URL for the 32M dataset
url = "https://files.grouplens.org/datasets/movielens/ml-32m.zip"
zip_path = "ml-32m.zip"
extract_path = "data/"

# 2. Download the file
print("Downloading MovieLens 32M (this may take a few minutes)...")
response = requests.get(url, stream=True)
with open(zip_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# 3. Extract the ZIP
print("Extracting files...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Done! Files are in the '{extract_path}ml-32m/' folder.")