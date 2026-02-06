import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec

def compute_tfidf(corpus: list[str], max_features: int = 1000, **kwargs):
    """
    Computes TF-IDF features from a corpus of text.
    
    Args:
        corpus: List of text documents.
        max_features: Maximum number of features to keep.
        **kwargs: Additional arguments passed to TfidfVectorizer.
        
    Returns:
        transformed_data: Sparse matrix of TF-IDF features.
        vectorizer: Fitted TfidfVectorizer object.
    """
    vectorizer = TfidfVectorizer(max_features=max_features, **kwargs)
    transformed_data = vectorizer.fit_transform(corpus)
    return transformed_data, vectorizer

def compute_doc_embeddings(tokens_series: pd.Series, model_path: str = 'outputs/models/word2vec_yelp.model', vector_size: int = 100):
    """
    Compute document embeddings by averaging word vectors.
    
    Args:
        tokens_series: Pandas Series containing lists of tokens.
        model_path: Path to the pre-trained Word2Vec model.
        vector_size: Size of the word vectors (used for fallback if model not loaded).
        
    Returns:
        embeddings: Numpy array of shape (n_docs, vector_size).
    """
    try:
        model = Word2Vec.load(model_path)
        print(f"Loaded Word2Vec model from {model_path}")
        vector_size = model.vector_size
    except Exception as e:
        print(f"Warning: Could not load model from {model_path} ({e}). using random initialization or zeros.")
        return np.zeros((len(tokens_series), vector_size))
        
    embeddings = []
    
    for tokens in tokens_series:
        if not isinstance(tokens, list):
             # Try to tokenize if it's a string, or handle empty/NaN
             if isinstance(tokens, str):
                 tokens = tokens.split() # Basic split as fallback
             else:
                 tokens = []
                 
        valid_vectors = [model.wv[word] for word in tokens if word in model.wv]
        
        if valid_vectors:
            doc_embedding = np.mean(valid_vectors, axis=0)
        else:
            doc_embedding = np.zeros(vector_size)
            
        embeddings.append(doc_embedding)
        
    return np.array(embeddings)
