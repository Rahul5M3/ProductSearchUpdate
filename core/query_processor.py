from config import USE_LLM_REPHRASING, T5_MODEL_NAME
from transformers import T5Tokenizer, TFT5ForConditionalGeneration
import tensorflow as tf

if USE_LLM_REPHRASING:
    tokenizer = T5Tokenizer.from_pretrained(T5_MODEL_NAME)
    model = TFT5ForConditionalGeneration.from_pretrained(T5_MODEL_NAME)

def rephrase(query: str) -> str:
    if not USE_LLM_REPHRASING:
        print(1)
        return query

    try:
        print(2)
        input_text = f"rephrase: {query}"
        input_ids = tokenizer.encode(input_text, return_tensors="tf")

        outputs = model.generate(
            input_ids=input_ids,
            max_new_tokens=32,
            num_beams=4,
            early_stopping=True
        )
        print(3)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        print(f"[ERROR] Rephrasing failed: {e}")
        return query    
    
# print(rephrase("Vivid Frying Pan with high quality"))    