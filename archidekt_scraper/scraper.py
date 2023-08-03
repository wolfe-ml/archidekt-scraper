import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
from archidekt_scraper.config import BASE_URL
from archidekt_scraper.models import Deck


def get_page_deck_list(page: int, sort_query: str):
    """get_page_deck_list"""
    url = f"{BASE_URL}/search/decks?orderBy={sort_query}&page={page}"
    session_requests = requests.session()
    deck_list_web = session_requests.get(url)
    deck_list_soup = BeautifulSoup(deck_list_web.content, "html.parser")
    results = deck_list_soup.findAll(class_="deckLink_thumbnail__aJFu7")
    links = [result["href"] for result in results]
    return links


def get_deck_list(
    num_decks: int,
    sort_query: str,
):
    """get_deck_list"""
    links = []
    page = 1
    pbar = tqdm(total=num_decks)
    while len(links) < num_decks:
        new_links = get_page_deck_list(page, sort_query)
        links.extend(new_links)
        pbar.update(len(new_links))
        page += 1
    deck_list = links[:num_decks]
    return deck_list


def get_deck_dataset(dataset_name: str, num_decks: int, sort_query: str):
    """get_deck_dataset"""

    # check validity of the output dataset path
    dataset_path = os.path.join(os.getcwd(), "datasets", dataset_name)
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
        os.makedirs(os.path.join(dataset_path, "decks"))

    # get a list of all the decks from the query
    decklist_file_path = os.path.join(dataset_path, "_decklist.json")
    deck_list = get_deck_list(num_decks, sort_query)

    with open(decklist_file_path, "w", encoding="utf8") as f:
        json.dump(deck_list, f, indent=4)

    # for each deck, get the deck info and save it to a file in the dataset path
    deck_dataset = []
    for i, link in enumerate(tqdm(deck_list)):
        file_path = os.path.join(dataset_path, "decks", f"{i}.json")
        deck = Deck.from_link(link, file_path)
        deck_dataset.append(deck)

    return deck_dataset
