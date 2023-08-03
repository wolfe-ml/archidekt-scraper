# Archidekt Web Scraper

This is a python app to scrape decks from Archidekt. Currently this reads through all the pages in `archidect.com/decks/{query}` until the amount of desired decks N is reached. The decks are parsed and saved to the directory in the input `dataset_name` parameter.

**Support Archidekt**: https://www.patreon.com/archidekt

## Installation

using pipenv:

    pipenv install

## Usage

    usage: run_scraper.py [-h] [--query query] N datset_name

    Scrape archidekt for deck info

    positional arguments:
    N              The number of decks to scrape and save.
    datset_name    The name of the deck dataset that will be saved locally

    options:
    -h, --help     show this help message and exit
    --query query  The search query to iterate through.

