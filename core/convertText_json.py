import json
import os

def parse_amazon_txt(file_path):
    products = []
    with open(file_path, 'r', encoding='utf-8') as f:
        product = {}
        for line in f:
            line = line.strip()
            if line.startswith("ITEM"):
                if product:
                    products.append(product)
                    product = {}
            elif '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                if key in product:
                    if isinstance(product[key], list):
                        product[key].append(value)
                    else:
                        product[key] = [product[key], value]
                else:
                    product[key] = value
        if product:
            products.append(product)
 
    return products[:600]

# Usage
INPUT_FILE1=os.path.normpath(os.path.join(os.path.dirname(__file__),'..','data','amazondata_Phones.txt'))
INPUT_FILE2=os.path.normpath(os.path.join(os.path.dirname(__file__),'..','data','amazondata_Electronics.txt'))
INPUT_FILE3=os.path.normpath(os.path.join(os.path.dirname(__file__),'..','data','amazondata_Automotive.txt'))
OUTPUT_FILE=OUTPUT_FILE=os.path.normpath(os.path.join(os.path.dirname(__file__),'..','data','amazondata.json'))

input_file = [INPUT_FILE1, INPUT_FILE2, INPUT_FILE3]
output_file = OUTPUT_FILE

for file in input_file:
    data=""
    data = parse_amazon_txt(os.path.normpath(file))
    with open(output_file, 'a', encoding='utf-8') as f:
        if f.tell() == 0:
            json.dump(data, f, indent=2)
        else :
            f.write('\n')
            json.dump(data, f, indent=2)


# print(input_file)