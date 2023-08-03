from dataclasses import dataclass
from typing import List
import json
from archidekt_scraper.config import BASE_URL
import requests
from bs4 import BeautifulSoup


@dataclass
class Card:
    name: str
    castingCost: List[str]
    colorIdentity: List[str]
    colors: List[str]
    text: str
    qty: int
    cardId: str
    subTypes: List[str]
    types: List[str]
    power: str
    toughness: str
    loyalty: str
    rarity: str
    flavor: str = ""

    @classmethod
    def from_dict(cls, env):
        return cls(
            **{k: v for k, v in env.items() if k in cls.__dataclass_fields__.keys()}
        )


@dataclass
class Deck:
    name: str
    description: str
    cards: List[Card]
    format: str
    link: str

    @classmethod
    def from_dict(cls, env):
        return cls(
            **{k: v for k, v in env.items() if k in cls.__dataclass_fields__.keys()}
        )

    def dict(self):
        out = self.__dict__
        out["cards"] = [card.__dict__ for card in self.cards]
        return out

    @classmethod
    def from_link(cls, deck_link, output_file=None):
        """get_deck_info"""

        # specify the deck URL
        url = f"{BASE_URL}{deck_link}"

        # get the html from the URL
        session_requests = requests.session()
        deck_info_web = session_requests.get(url)

        # parse the HTML from the URL
        deck_info_soup = BeautifulSoup(deck_info_web.content, "html.parser")
        deck_info = json.loads(deck_info_soup.find(id="__NEXT_DATA__").text)
        deck_info = deck_info["props"]["pageProps"]["redux"]["deck"]
        cards = deck_info["cardMap"]

        deck_info["cards"] = [Card.from_dict(card) for card in cards.values()]
        deck_info["link"] = url

        deck = cls.from_dict(deck_info)

        if output_file is not None:
            deck.save(output_file)

        return deck

    def save(self, file_path: str):
        with open(file_path, "w", encoding="utf8") as f:
            json.dump(self.dict(), f, indent=4)
