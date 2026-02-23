"""
Tests unitaires pour src/text_preprocessing.py
"""

import pytest
from src.text_preprocessing import (
    clean_text,
    remove_urls_emails,
    remove_stopwords,
    tokenize_text,
    lemmatize_tokens,
    preprocess_pipeline,
)


# --- clean_text ---

class TestCleanText:
    def test_lowercase(self):
        assert clean_text("HELLO WORLD") == "hello world"

    def test_remove_punctuation(self):
        result = clean_text("Hello, world! How's it going?")
        assert "," not in result
        assert "!" not in result
        assert "'" not in result

    def test_remove_url(self):
        result = clean_text("Visit http://example.com for more")
        assert "http" not in result
        assert "example" not in result

    def test_remove_email(self):
        result = clean_text("Contact me at user@test.com please")
        assert "@" not in result

    def test_keep_alphanumeric(self):
        result = clean_text("Room 101 is great")
        assert "101" in result
        assert "room" in result

    def test_empty_string(self):
        assert clean_text("") == ""


# --- remove_urls_emails ---

class TestRemoveUrlsEmails:
    def test_url_http(self):
        assert "http" not in remove_urls_emails("Go to http://site.com now")

    def test_url_www(self):
        assert "www" not in remove_urls_emails("Go to www.site.com now")

    def test_email(self):
        assert "@" not in remove_urls_emails("Email me@test.com")

    def test_no_urls(self):
        text = "Just a normal sentence"
        assert remove_urls_emails(text) == text


# --- tokenize_text ---

class TestTokenizeText:
    def test_basic(self):
        tokens = tokenize_text("hello world")
        assert tokens == ["hello", "world"]

    def test_returns_list(self):
        assert isinstance(tokenize_text("test"), list)


# --- lemmatize_tokens ---

class TestLemmatizeTokens:
    def test_plural(self):
        result = lemmatize_tokens(["cats", "dogs"])
        assert "cat" in result
        assert "dog" in result

    def test_already_lemma(self):
        assert lemmatize_tokens(["run"]) == ["run"]


# --- remove_stopwords ---

class TestRemoveStopwords:
    def test_removes_common(self):
        tokens = ["the", "cat", "is", "here"]
        result = remove_stopwords(tokens)
        assert "the" not in result
        assert "is" not in result
        assert "cat" in result

    def test_exclude_negation(self):
        tokens = ["not", "good"]
        result = remove_stopwords(tokens, exclude={"not"})
        assert "not" in result

    def test_empty_list(self):
        assert remove_stopwords([]) == []


# --- preprocess_pipeline ---

class TestPreprocessPipeline:
    def test_returns_list(self):
        result = preprocess_pipeline("The cats are running quickly")
        assert isinstance(result, list)

    def test_removes_stopwords_by_default(self):
        result = preprocess_pipeline("The cat is here")
        assert "the" not in result
        assert "is" not in result

    def test_no_stopword_removal(self):
        result = preprocess_pipeline("The cat is here", remove_stopwords_flag=False)
        assert "the" in result

    def test_no_lemmatization(self):
        result = preprocess_pipeline("cats dogs", lemmatize_flag=False)
        assert "cats" in result

    def test_full_pipeline(self):
        text = "Visit http://example.com! The CATS are running."
        result = preprocess_pipeline(text)
        assert isinstance(result, list)
        assert len(result) > 0
        # URL removed, lowercased, lemmatized
        assert "http" not in " ".join(result)
