# eBaydle
Worlde game where users are prompted with a web scrapped ebay item and have to correctly guess the price. Prompted with a higher or lower message when entering an incorrect guess.

Still in early stages of development.
Products and their data are successfully scraped from ebay and added to a MongoDB database. Frontend is built with react and typescript, using axios to handle HTTP requests to backend. Backend is built with Node.js and Express utilizing typescript.

## Pip Scraping Libraries Installation
To install the libraries required to scrape, run this command:
```sh
pip install -r libraries.txt
```

Dictionary used to return random words taken from 'https://github.com/nightblade9/simple-english-dictionary/blob/main/processed/merged.json'
