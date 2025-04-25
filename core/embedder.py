# from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBEDDING_MODEL
from transformers import TFAutoModel, AutoTokenizer
import tensorflow as tf

# model= SentenceTransformer(EMBEDDING_MODEL,from_tf=True)

tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)
model = TFAutoModel.from_pretrained(EMBEDDING_MODEL)

def get_embedding(text: str) -> np.ndarray:
    # embedding = model.encode(text, convert_to_numpy=True)
    inputs = tokenizer(text,padding=True,return_tensors="tf")
    outputs = model.encoder(**inputs)  # Not generate
    sentence_embedding = tf.reduce_mean(outputs.last_hidden_state, axis=1)
    return sentence_embedding.numpy()

def get_batch_embeddings(text: list[str]) -> np.ndarray:
    # embedding = model.encode(text, convert_to_numpy=True)
    # return embedding
    inputs = tokenizer(text,padding=True,return_tensors="tf")
    outputs = model.encoder(**inputs)  # Not generate
    sentence_embedding = tf.reduce_mean(outputs.last_hidden_state, axis=1)
    return sentence_embedding.numpy()