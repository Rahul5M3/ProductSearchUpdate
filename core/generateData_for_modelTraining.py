import json
import os
import random

products=[]

with open(os.path.join(os.path.dirname(__file__),'..','data',"data1_info.txt"), "r") as f:
    for line in f:
        if line.strip():  # Skip empty lines
            try:
                data = json.loads(line.strip())
                products.append(data)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)

def create_queries(product):
    keywords = product["description"].split() + product["specification"].split() + product["original_specification"].split() + product["original_description"].split() + product["productName"].split() + product["category"].split()
    random.shuffle(keywords)
    queries = []
    targets=[]
    for _ in range(6):
        k = random.randint(6, 12)
        random.shuffle(keywords)
        query = " ".join(keywords[:k])
        queries.append(f"product_query: {query.lower()}")
        targets.append(f"Description: {product['description'].lower()}. Specification: {product['specification'].lower()}")
    return queries,targets                

with open(os.path.join(os.path.dirname(__file__),'..','data','modelTrainingData.txt'), 'w', encoding="utf-8") as f:
    for product in products:
        queries,targets=create_queries(product)
        for query,target in zip(queries,targets):
            f.write(json.dumps({"input": query, "target": target}) + "\n")