import json
import os
import re
from add_synonyms import expand_query_with_synonyms

with open(os.path.join(os.path.dirname(__file__),'..','data','moreProducts.json'), 'r', encoding="utf-8") as f:
    data=json.load(f)

descriptions=[]
for item in data:
    if item.get('specification'):
        features=[ f.strip() for feature in item["specification"] if feature is not None for f in feature.split(',') ]
        features=" ".join(features).replace('-','').replace('  ', ' ')
    else:
        features=""

    if item.get('description')==None:
        continue
    
    synFeatures=expand_query_with_synonyms(features, max_synonyms_per_word=2, max_expansions=5)
    synDescriptions=expand_query_with_synonyms(item['description'].replace('-','').replace('  ', ' '), max_synonyms_per_word=2, max_expansions=5)

    for  synFeature in synFeatures:
        for synDescription in synDescriptions:
            if synFeature==None or synDescription==None:
                continue
            descriptions.append({"category": item['category'], "productName": item['productName'], "description": synDescription, "specification": synFeature, "original_description": item['description'], "original_specification": features})
    descriptions.append({"category": item['category'], "productName": item['productName'], "description": item['description'], "specification": features, "original_description": item['description'], "original_specification": features})

    # descriptions.append((item['Title'] + " " + item['Brand'] + " " + item['ProductTypeName'] + " " + item['ProductGroup'] + " " + features).replace("  ", " "))
# descriptions=[f" {item['Title']} {item['ProductTypeName']} {item['Feature'].replace('\n', ' ') if item.get('detail') else ''} {item['Brand']} {item['ProductGroup']} " for item in data]
# descriptions=[]
# for (i, item) in enumerate(data[2]['data']):
#     if item.get('detail'):
#         detail=item['detail'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
#         detail=detail.replace('  ', ' ').replace('  ', ' ')
#         detail=re.sub(r'https?://\S+', '', detail)
#         descriptions.append(f" {item['product_name']} {item['catg1']} {detail} ")
#     else:
#         descriptions.append(f" {item['product_name']} {item['catg1']} ")

with open(os.path.join(os.path.dirname(__file__),'..','data','data1_info.txt'), 'w', encoding="utf-8") as f:
    for desc in descriptions:
        f.write(json.dumps(desc) + "\n")

print("Descriptions saved to data1_info.txt")        

# print(descriptions[1])