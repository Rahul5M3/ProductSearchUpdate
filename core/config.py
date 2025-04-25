import os

USE_LLM_REPHRASING = True
USE_SYNONYM_EXPANSION = False

# T5_MODEL_NAME = "t5-base"
# EMBEDDING_MODEL = "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"

# T5_MODEL_NAME=os.path.join(os.path.dirname(__file__),'..','model','t1_product_generator6')
# EMBEDDING_MODEL= os.path.join(os.path.dirname(__file__),'..','model','t1_product_generator6')
# T5_MODEL_NAME=os.path.join(os.path.dirname(__file__),'..','model','t53-product-generator')
# EMBEDDING_MODEL= os.path.join(os.path.dirname(__file__),'..','model','t53-product-generator')

T5_MODEL_NAME=os.path.join(os.path.dirname(__file__),'..','model','tnew1_product_generator_zip')
EMBEDDING_MODEL= os.path.join(os.path.dirname(__file__),'..','model','tnew1_product_generator_zip')

PRODUCT_DATASET_PATH = os.path.join(os.path.dirname(__file__),'..','data','moreProducts.json')
SPELL_DICT_PATH = os.path.join(os.path.dirname(__file__),'..','data','data1_freq.txt')

TOP_K = 5
