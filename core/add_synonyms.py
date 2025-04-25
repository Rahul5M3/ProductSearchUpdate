import nltk
from nltk.corpus import wordnet
import random

nltk.download('wordnet')
nltk.download('omw-1.4')

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            lemma_name = lemma.name().replace("_", " ").lower()
            if lemma_name != word.lower():
                synonyms.add(lemma_name)
    return list(synonyms)

def expand_query_with_synonyms(query, max_synonyms_per_word=2, max_expansions=5):
    words = query.split()
    expanded_queries = set()
    
    for i, word in enumerate(words):
        syns = get_synonyms(word)
        random.shuffle(syns)  # Shuffle to get different combos
        for synonym in syns[:max_synonyms_per_word]:
            new_words = words.copy()
            new_words[i] = synonym
            new_query = " ".join(new_words)
            if new_query != query:
                expanded_queries.add(new_query)
            if len(expanded_queries) >= max_expansions:
                break
        if len(expanded_queries) >= max_expansions:
            break

    return list(expanded_queries)