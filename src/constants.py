"""
Constantes partagées pour le projet S6C01.
"""

RANDOM_STATE = 42
SAMPLE_SIZE = 10_000

# Labels
POLARITY_NAMES = ['Négatif', 'Neutre', 'Positif']
SCORE_NAMES = ['1★', '2★', '3★', '4★', '5★']


def stars_to_polarity(stars):
    """Convertit un score 1-5 en polarité 0/1/2."""
    if stars <= 2:
        return 0
    elif stars == 3:
        return 1
    else:
        return 2
