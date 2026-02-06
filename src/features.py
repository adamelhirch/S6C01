import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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
