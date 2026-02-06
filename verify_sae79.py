
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from pathlib import Path

# Paths
EMBEDDINGS_PATH = Path('outputs/doc_embeddings_w2v.npy')
REVIEWS_PATH = Path('data/cleaned/reviews_clean.parquet')
FIGURES_PATH = Path('outputs/figures')
FIGURES_PATH.mkdir(parents=True, exist_ok=True)

print(f"📂 Verification script started from: {Path.cwd()}")

# Load small sample of embeddings
try:
    full_embeddings = np.load(EMBEDDINGS_PATH, mmap_mode='r')
    print(f"✅ Embeddings found: {full_embeddings.shape}")
    sample_size = 100
    embeddings_sample = full_embeddings[:sample_size]
    
    # Load corresponding stars
    df_reviews = pd.read_parquet(REVIEWS_PATH).head(sample_size)
    ratings_sample = df_reviews['stars'].values
    print(f"✅ Ratings loaded: {len(ratings_sample)}")
    
    # Run Quick t-SNE
    print("⏳ Running mini t-SNE...")
    tsne = TSNE(n_components=2, perplexity=5, n_iter=250, random_state=42)
    X_embedded = tsne.fit_transform(embeddings_sample)
    print("✅ t-SNE computed.")
    
    # Generate Dummy Plot
    plt.figure(figsize=(5, 5))
    plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=ratings_sample)
    output_file = FIGURES_PATH / 'verify_tsne.png'
    plt.savefig(output_file)
    print(f"✅ Test Plot saved: {output_file}")
    
except Exception as e:
    print(f"❌ Verification failed: {e}")
    exit(1)
