from collections import Counter
import re
import os
import json
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.corpus import stopwords
import nltk
import string

nltk.download('stopwords')

# with open(os.path.join(os.path.dirname(__file__),'..','data','amazondata.json'), "r", encoding="utf-8") as f:
#     products=json.load(f)

products = []

with open(os.path.join(os.path.dirname(__file__),'..','data',"data1_info.txt"), "r") as f:
    for line in f:
        if line.strip():  # Skip empty lines
            try:
                data = json.loads(line.strip())
                products.append(data)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)

# for product in products:
#     if product.get('original_description') is None:
#         print('yeah none')
#         break
        
# product_txt= [ product['category'] + " " + product['productName'] + " " + product['description'] +  " " + product['specification'] + " " + product.get('original_description') + " " + product.get('original_specification')   for product in products]   

product_txt=[]
# # i=0
for product in products:  

    if product.get('original_description') is None:
        continue

    if product.get('original_specification') is None:
        continue


    product_txt.append((product['category'] + " " + product['productName'] + " " + product['description'] + " " + product['specification'] + " " + product['original_description'] + " " + product['original_specification']).replace("  ", " "))

def custom_tokenizer(text):
    text = re.sub(r'-', ' ', text)  
    return word_tokenize(text.lower())

tokens=[custom_tokenizer(text.lower()) for text in product_txt]

flat_tokens = list(chain.from_iterable(tokens))

stop_words = set(stopwords.words("english"))
punctuation = set(string.punctuation)

filtered_tokens = [
    word for word in flat_tokens
    if  word.strip() not in punctuation and word.strip().isalnum() and not word.strip().isnumeric()
]

        

product_freq=dict(Counter(filtered_tokens))

dictionary_path = os.path.join(os.path.dirname(__file__),"..","data", "data1_freq.txt")

existing_dict = {}

if os.path.exists(dictionary_path):
    with open(dictionary_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2 and parts[1].isdigit():
                word, freq = parts
                existing_dict[word] = int(freq)

for word, freq in product_freq.items():
    if word in existing_dict:
        existing_dict[word] += freq
    else:
        existing_dict[word] = freq                

with open(dictionary_path, "w", encoding="utf-8") as f:
    for word, freq in sorted(existing_dict.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{word} {freq}\n")

