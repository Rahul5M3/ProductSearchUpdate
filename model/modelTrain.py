from datasets import Dataset
import os
from transformers import T5Tokenizer
# from transformers import DataCollatorForT5MLM
from transformers import TFT5ForConditionalGeneration
import tensorflow as tf
import random
import json

import spacy
nlp = spacy.load("en_core_web_sm")

with open(os.path.join(os.path.dirname(__file__),'..','data','data1_info.txt'),'r') as f:
    # texts = [line.strip() for line in f if line.strip()]
    texts = [json.loads(line.strip()) for line in f if line.strip()]

# print(texts[0])

# def create_prompt(desc):
#     doc=nlp(desc)
#     nouns = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
#     # noun_chunk = [chunk.text for chunk in doc.noun_chunks][:2]
#     # random_elements = random.sample(nouns, min(2, len(nouns)))
#     return " ".join(nouns)




# data=[]
# for text in texts:
#     if(text)

# data=[]
# i=0
# for text in texts:
#     print(i)
#     if(text.get('original_description')==None):
#         print(text)
#         break
#     i=i+1

# data = [{"input": f"query: {text['description'].lower()} {text['specification'].ower()} ", "target": f" {text['original_description'].lower()} {text['original_specification'].lower()} "} for text in texts]
# dataset = Dataset.from_list(data)

# tokenizer = T5Tokenizer.from_pretrained("t5-base")

# def tokenize(example):
#     input_enc = tokenizer(example["input"], padding="max_length", truncation=True, max_length=42)
#     target_enc = tokenizer(example["target"], padding="max_length", truncation=True, max_length=74)

#     labels = target_enc["input_ids"]
#     labels = [l if l != tokenizer.pad_token_id else -100 for l in labels]
#     return {
#         "input_ids": input_enc["input_ids"],
#         "attention_mask": input_enc["attention_mask"],
#         "labels": labels
#     }

# tokenized_dataset = dataset.map(tokenize)

# model = TFT5ForConditionalGeneration.from_pretrained("t5-base")

# tf_dataset = tokenized_dataset.to_tf_dataset(
#     columns=["input_ids", "attention_mask", "labels"],
#     shuffle=True,
#     batch_size=10,

#     collate_fn=lambda x: {
#         "input_ids": tf.convert_to_tensor([f["input_ids"] for f in x], dtype=tf.int32),
#         "attention_mask": tf.convert_to_tensor([f["attention_mask"] for f in x], dtype=tf.int32),
#         "labels": tf.convert_to_tensor([f["labels"] for f in x], dtype=tf.int32),
#     }
# )

# optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
# model.compile(optimizer=optimizer)
# model.fit(tf_dataset, epochs=2)

# model.save_pretrained(os.path.dirname(__file__),".","tnew1_product_generator")
# tokenizer.save_pretrained(os.path.dirname(__file__),".","tnew1_product_generator")
