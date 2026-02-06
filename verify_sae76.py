
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import time

# Configuration paths - adjusting for scripts/ location
# Assuming script is run from root 'c:\Users\natal\Documents\BUT3\Semestre2\S6C01\S6C01'
DATA_PATH = Path('data/cleaned/reviews_text_cleaned.parquet')
MODEL_PATH = Path('outputs/models/tfidf_vectorizer.pkl')

print(f"📂 Loading: {DATA_PATH}")

if not DATA_PATH.exists():
    print(f"❌ File not found: {DATA_PATH.absolute()}")
    exit(1)

# Limit rows for speed in verification if needed, but let's try full
df = pd.read_parquet(DATA_PATH).head(10000) 
# df = pd.read_parquet(DATA_PATH)
print(f"✅ Data loaded: {len(df):,} reviews")

if 'text_cleaned' not in df.columns:
    print("❌ Column 'text_cleaned' missing!")
    exit(1)

df['text_cleaned'] = df['text_cleaned'].fillna('')

# Define vectorizers
vectorizers = {
    "Default": TfidfVectorizer(max_features=100), # Reduced for speed test
    "Limited": TfidfVectorizer(max_features=100, min_df=5, max_df=0.8),
    "Bigrams": TfidfVectorizer(max_features=100, ngram_range=(1, 2), min_df=5)
}

# Real values for final save
final_vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    min_df=5
)

print("🚀 Starting verification processing...")

# Test the final one
try:
    print("⏳ Fitting final Bigrams model...")
    vect = final_vectorizer
    X = vect.fit_transform(df['text_cleaned'])
    sparsity = (1 - X.nnz / (X.shape[0] * X.shape[1])) * 100
    print(f"   Shape: {X.shape}")
    print(f"   Sparsity: {sparsity:.2f}%")
    
    # Save
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(vect, f)
    print(f"✅ Model saved to {MODEL_PATH}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
