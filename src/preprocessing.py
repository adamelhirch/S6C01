"""
Fonctions de preprocessing NLP pour les avis textuels
"""
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def clean_text(text):
    """
    Nettoyage basique du texte

    Args:
        text: Texte brut

    Returns:
        Texte nettoyé
    """
    if pd.isna(text):
        return ""

    # Lowercase
    text = text.lower()

    # Supprimer URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Supprimer emails
    text = re.sub(r'\S+@\S+', '', text)

    # Supprimer ponctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Supprimer espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def preprocess_pipeline(text, remove_stopwords=True, lemmatize=True):
    """
    Pipeline complet de preprocessing NLP

    Args:
        text: Texte brut
        remove_stopwords: Supprimer les stopwords
        lemmatize: Lemmatiser les mots

    Returns:
        Texte preprocessé
    """
    # 1. Nettoyage
    text = clean_text(text)

    # 2. Tokenization
    tokens = word_tokenize(text)

    # 3. Stopwords
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words]

    # 4. Lemmatization
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return ' '.join(tokens)
