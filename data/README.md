# Dossier Data

Ce dossier contient les données du projet Yelp.

## ⚠️ Important

**Les fichiers de données ne sont PAS versionnés sur Git** (trop volumineux).

## Structure

```
data/
├── raw/                    # Données brutes JSON (NON versionnées)
│   ├── yelp_academic_dataset_business.json
│   ├── yelp_academic_reviews4students.jsonl
│   └── yelp_academic_dataset_user4students.jsonl
│
└── cleaned/                # Données nettoyées en parquet (NON versionnées)
    ├── business_clean.parquet
    ├── reviews_clean.parquet
    └── users_clean.parquet
```

## Installation des données

1. Téléchargez les fichiers JSON depuis le sujet
2. Placez-les dans `data/raw/`
3. Exécutez les notebooks de nettoyage pour générer les fichiers dans `data/cleaned/`

## Fichiers générés

Les fichiers `.parquet` sont générés par les notebooks suivants:
- `business_clean.parquet` → SAE-96 (Nettoyage Business)
- `reviews_clean.parquet` → SAE-97 (Nettoyage Reviews)
- `users_clean.parquet` → SAE-98 (Nettoyage Users)

## Format Parquet

Parquet est un format de fichier columnar optimisé pour:
- ✅ Compression efficace (fichiers plus petits)
- ✅ Chargement rapide
- ✅ Compatible avec pandas, polars, etc.
- ✅ Préserve les types de données
