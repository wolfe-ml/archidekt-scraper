from archidekt_scraper.scraper import get_deck_dataset
from archidekt_scraper.config import DEFAULT_SORT_QUERY, DEFAULT_N, DEFAULT_DATASET_NAME
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape archidekt for deck info")
    parser.add_argument(
        "num_decks",
        metavar="N",
        type=int,
        default=DEFAULT_N,
        help="The number of decks to scrape and save.",
    )
    parser.add_argument(
        "dataset_name",
        metavar="datset_name",
        type=str,
        default=DEFAULT_DATASET_NAME,
        help="The name of the deck dataset that will be saved locally",
    )
    parser.add_argument(
        "--query",
        metavar="query",
        type=str,
        default=DEFAULT_SORT_QUERY,
        help="The search query to iterate through.",
        required=False,
    )
    args = parser.parse_args()

    get_deck_dataset(args.dataset_name, args.num_decks, args.query)
