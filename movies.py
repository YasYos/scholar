import os
import re
import string
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

def load_imdb_data(folder):
    data = []
    labels = []
    
    for label_type in ['pos', 'neg']:
        path = os.path.join(folder, label_type)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                review = f.read()
                data.append(clean_text(review))
                labels.append(1 if label_type == 'pos' else 0)

    return pd.DataFrame({'review': data, 'label': labels})

train_data = load_imdb_data("aclImdb/train")
test_data = load_imdb_data("aclImdb/test")

train_data.to_csv("processed_train.csv", index=False)
test_data.to_csv("processed_test.csv", index=False)
