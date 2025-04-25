import json
import os
import numpy as np
import faiss
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
from config import PRODUCT_DATASET_PATH, TOP_K

from embedder import get_embedding, get_batch_embeddings

def load_products():
    with open(PRODUCT_DATASET_PATH, "r", encoding="utf-8") as f:
        products = json.load(f)
    return products

def faissAndBM25(products: list):
    product_txt= [ product['productName'] + " " + product['category'] + " " + product['description'] + " " + " ".join([item for p in product['specification'] for item in p.split(',')])  for product in products]   

    print("Generating embeddings for products...")
    products_embedding=get_batch_embeddings(product_txt).astype('float32')

    embedding_dim=products_embedding.shape[1]

    #faiss
    faiss.normalize_L2(products_embedding)

    nlist = 20 # number of clusters
    quantizer = faiss.IndexFlatL2(embedding_dim)  # Use L2 distance for clustering
    index = faiss.IndexIVFFlat(quantizer, embedding_dim, nlist, faiss.METRIC_L2)
    index.train(products_embedding)
    index.add(products_embedding)
    print("Index trained and added to FAISS index.")

    # ----------- BM25 Indexing -----------
    print("Preparing BM25 index...")
    tokens_prod=[word_tokenize(text.lower()) for text in product_txt]

    bm25 = BM25Okapi(tokens_prod)

    return  index, bm25, products_embedding

# ----------- Search Function -----------

def search_top_k(query:str, products: list, k: int = TOP_K)-> list:

    index, bm25, products_embedding = faissAndBM25(products)

    query_embedding=get_embedding(query).astype('float32').reshape(1,-1)
    _, faiss_indices=index.search(query_embedding,k)

    query_tokens=word_tokenize(query.lower())
    scores=bm25.get_scores(query_tokens)
    top_k_indices=np.argsort(scores)[::-1][:k]

    all_index = list(set(map(int, faiss_indices.flatten().tolist())) | set(map(int, top_k_indices.flatten().tolist())))
    results = []

    for idx in all_index:
        faiss_score=-np.linalg.norm(products_embedding[idx]-query_embedding)
        bm25_score=bm25.get_scores(query_tokens)[idx]
        hybrid_score = faiss_score + (0.3 * bm25_score)
        results.append((hybrid_score, products[idx]))


    results=sorted(results, key=lambda x:x[0], reverse=True)[:k]    

    return [{"product":result[1], "score":result[0]} for result in results]

# print(search_top_k("description: bright highquality frying pan for everyday use.. specification: nonstick coating dish washer safe even heat distribution 2year warranty",load_products(), 5))