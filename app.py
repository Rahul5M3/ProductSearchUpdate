from fastapi import FastAPI,Query
from pydantic import BaseModel
from core.spell_corrector import correct_spelling
from core.query_processor import rephrase
from core.retriever import load_products, search_top_k
from typing import List

app = FastAPI(title="Product Recommendation Chatbot")

products = load_products()

class QueryInput(BaseModel):
    query: str

class Product(BaseModel):
    productName: str
    description: str
    specification: List[str]
    category: str

class SearchResponse(BaseModel):
    processed_query: str
    results: List[Product]

@app.post('/search', response_model=SearchResponse)
def search_products(q:str=Query(...,description="User query")):
    """
    Search for products based on the user query.
    """
    # Correct spelling in the query
    corrected_query = correct_spelling(q)
    
    # Rephrase the query if necessary
    rephrased_query = rephrase(corrected_query)

    # Search for top K products
    results = search_top_k(rephrased_query, products)

    # Prepare the response
    response = {
        "processed_query": rephrased_query,
        "results": results
    }

    return response