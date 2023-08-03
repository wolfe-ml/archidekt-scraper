import os

BASE_URL = os.getenv("BASE_URL", "https://archidekt.com")
DEFAULT_N = int(os.getenv("NUM_DECKS", "1000"))
DEFAULT_DATASET_NAME = os.getenv("DATASET_NAME", "deck_dataset")
DEFAULT_SORT_QUERY = os.getenv("SORT_QUERY", "-viewCount")
