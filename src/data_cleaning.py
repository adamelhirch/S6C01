"""
Fonctions de nettoyage des données JSON Yelp
"""
import pandas as pd
import numpy as np


def clean_business_data(df):
    """
    Nettoie le DataFrame business

    Args:
        df: DataFrame business brut

    Returns:
        DataFrame nettoyé
    """
    df = df.copy()

    # 1. Supprimer doublons
    df = df.drop_duplicates(subset=['business_id'])

    # 2. Traiter valeurs manquantes
    df['attributes'] = df['attributes'].fillna({})
    df['hours'] = df['hours'].fillna({})

    # 3. Split categories
    df['categories_list'] = df['categories'].str.split(', ')

    # 4. Convertir types
    df['stars'] = df['stars'].astype(float)
    df['is_open'] = df['is_open'].astype(bool)

    print(f"✅ Business nettoyé: {len(df)} commerces")
    return df


def clean_reviews_data(df):
    """
    Nettoie le DataFrame reviews

    Args:
        df: DataFrame reviews brut

    Returns:
        DataFrame nettoyé
    """
    df = df.copy()

    # 1. Supprimer reviews vides
    df = df[df['text'].notna()]
    df = df[df['text'].str.strip() != '']

    # 2. Calculer longueurs
    df['char_count'] = df['text'].str.len()
    df['word_count'] = df['text'].str.split().str.len()

    # 3. Filtrer reviews trop courtes
    df = df[df['char_count'] >= 10]

    # 4. Supprimer doublons
    df = df.drop_duplicates(subset=['review_id'])

    # 5. Valider stars
    df = df[df['stars'].between(1, 5)]

    # 6. Convertir dates
    df['date'] = pd.to_datetime(df['date'])

    print(f"✅ Reviews nettoyées: {len(df)} avis")
    return df


def clean_users_data(df):
    """
    Nettoie le DataFrame users

    Args:
        df: DataFrame users brut

    Returns:
        DataFrame nettoyé
    """
    df = df.copy()

    # 1. Supprimer doublons
    df = df.drop_duplicates(subset=['user_id'])

    # 2. Traiter valeurs manquantes
    df['review_count'] = df['review_count'].fillna(0)
    df['average_stars'] = df['average_stars'].fillna(0)

    # 3. Valider average_stars
    df = df[df['average_stars'].between(0, 5)]

    # 4. Segmentation expérience
    def segment_user(review_count):
        if review_count < 5:
            return 'nouveau'
        elif review_count < 50:
            return 'régulier'
        else:
            return 'expert'

    df['segment'] = df['review_count'].apply(segment_user)

    print(f"✅ Users nettoyés: {len(df)} utilisateurs")
    return df
