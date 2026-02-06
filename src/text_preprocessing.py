"""
Text preprocessing utilities for NLP tasks.

This module provides functions for cleaning, tokenizing, and normalizing
text data from Yelp reviews.
"""

import re
from typing import List, Set
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Initialize once to avoid repeated initialization
_lemmatizer = None
_stop_words = None


def _get_lemmatizer() -> WordNetLemmatizer:
    """Get or initialize the lemmatizer."""
    global _lemmatizer
    if _lemmatizer is None:
        _lemmatizer = WordNetLemmatizer()
    return _lemmatizer


def _get_stopwords() -> Set[str]:
    """Get or initialize English stopwords."""
    global _stop_words
    if _stop_words is None:
        _stop_words = set(stopwords.words('english'))
    return _stop_words


def remove_urls_emails(text: str) -> str:
    """
    Remove URLs and email addresses from text.
    
    Args:
        text: Input text
    
    Returns:
        Text with URLs and emails removed
    
    Example:
        >>> text = "Check out http://example.com or email me@test.com"
        >>> remove_urls_emails(text)
        'Check out  or email '
    """
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove emails
    text = re.sub(r'[\w\.-]+@[\w\.-]+', '', text)
    return text


def tokenize_and_lemmatize(text: str, remove_stops: bool = True) -> List[str]:
    """
    Tokenize text and apply lemmatization.
    
    Args:
        text: Input text
        remove_stops: Whether to remove stopwords (default: True)
    
    Returns:
        List of lemmatized tokens
    
    Example:
        >>> tokens = tokenize_and_lemmatize("The cats are running quickly")
        >>> print(tokens)
        ['cat', 'running', 'quickly']
    """
    lemmatizer = _get_lemmatizer()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Lemmatize
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Remove stopwords if requested
    if remove_stops:
        stop_words = _get_stopwords()
        tokens = [token for token in tokens if token not in stop_words]
    
    return tokens


def remove_stopwords(tokens: List[str], exclude: Set[str] = None) -> List[str]:
    """
    Remove English stopwords from token list.
    
    Args:
        tokens: List of tokens
        exclude: Set of words to exclude from removal (they will be KEPT in the text).
                 Useful for keeping negation words like 'no', 'not'.
    
    Returns:
        Filtered list without stopwords
    
    Example:
        >>> tokens = ['the', 'cat', 'is', 'not', 'here']
        >>> remove_stopwords(tokens, exclude={'not'})
        ['cat', 'not', 'here']
    """
    stop_words = _get_stopwords()
    
    if exclude:
        # Create a new set for this call to avoid modifying the global set
        current_stop_words = stop_words - set(exclude)
    else:
        current_stop_words = stop_words
        
    return [token for token in tokens if token.lower() not in current_stop_words]


def clean_text(text: str) -> str:
    """
    Basic text cleaning: lowercase, remove URLs/emails, keep only alphanumeric and spaces.
    
    Args:
        text: Input text
        
    Returns:
        Cleaned text string
    """
    # Lowercase
    text = text.lower()
    
    # Remove URLs and emails
    text = remove_urls_emails(text)
    
    # Keep only letters, numbers, spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    return text


def preprocess_text(text: str) -> str:
    """
    Legacy function: Clean and normalize text for NLP tasks.
    
    This function is maintained for backward compatibility.
    It performs: clean -> tokenize -> remove stopwords -> lemmatize -> join.
    """
    # 1. Clean
    text_clean = clean_text(text)
    
    # 2. Pipeline sequence
    tokens = tokenize_text(text_clean)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    
    return ' '.join(tokens)


def preprocess_pipeline(
    text: str, 
    remove_stopwords_flag: bool = True, 
    lemmatize_flag: bool = True,
    exclude_stopwords: Set[str] = None
) -> List[str]:
    """
    Complete preprocessing pipeline.
    
    Args:
        text: Input text
        remove_stopwords_flag: Whether to remove stopwords
        lemmatize_flag: Whether to lemmatize tokens
        exclude_stopwords: Set of words to keep (e.g. {'not', 'no'})
        
    Returns:
        List of processed tokens
    """
    # 1. Clean
    text = clean_text(text)
    
    # 2. Tokenize
    tokens = tokenize_text(text)
    
    # 3. Stopwords
    if remove_stopwords_flag:
        tokens = remove_stopwords(tokens, exclude=exclude_stopwords)
        
    # 4. Lemmatize
    if lemmatize_flag:
        tokens = lemmatize_tokens(tokens)
        
    return tokens


def tokenize_text(text: str) -> List[str]:
    """
    Tokenize text into a list of words using NLTK.
    
    Args:
        text: Input text
        
    Returns:
        List of tokens
        
    Example:
        >>> tokenize_text("Don't hesitate!")
        ['Do', "n't", 'hesitate', '!']
    """
    return word_tokenize(text)


def lemmatize_tokens(tokens: List[str]) -> List[str]:
    """
    Lemmatize a list of tokens.
    
    Args:
        tokens: List of tokens
        
    Returns:
        List of lemmatized tokens
        
    Example:
        >>> tokens = ['running', 'better', 'cars']
        >>> lemmatize_tokens(tokens)
        ['running', 'better', 'car'] 
        # Note: default NLTK lemmatizer treats words as nouns by default unless POS tags are provided
    """
    lemmatizer = _get_lemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]
