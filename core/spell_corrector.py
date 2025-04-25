import os
from symspellpy.symspellpy import SymSpell, Verbosity
import nltk
from nltk.corpus import wordnet
from transformers import pipeline, T5Tokenizer, TFT5ForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM
import tiktoken
from config import SPELL_DICT_PATH

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
sym_spell.load_dictionary(SPELL_DICT_PATH, term_index=0, count_index=1)

# def load_symspell_dict():
#     # dictionary_path = os.path.join(os.path.dirname(__file__), "frequency_dictionary_en_82_765.txt")
#     dictionary_path = os.path.join(os.path.dirname(__file__), "product_freq_dict.txt")
#     if os.path.exists(dictionary_path):
#         sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# # ----------- SPELLING CORRECTION -----------

def correct_spelling(query: str) -> str:
    suggestions=sym_spell.lookup_compound(query, max_edit_distance=2)
    return suggestions[0].term if suggestions else query 