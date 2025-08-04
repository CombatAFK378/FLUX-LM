 # download_model.py
import gensim.downloader as api

print("Downloading the model... This might take a few minutes.")
model = api.load("word2vec-google-news-300")
print("✅ Model downloaded and cached successfully.")
