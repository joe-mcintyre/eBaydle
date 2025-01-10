import json
import httpx
from parsel import Selector

session = httpx.Client(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    },
    http2=True,
    follow_redirects=True
)

def parse_search(response: httpx.Response) -> list:
    sel = Selector(response.text)
    css_join = lambda css: "".join(sel.css(css).getall()).strip()  # join all selected elements
    css = lambda css: sel.css(css).get("").strip() 

    searchList = []
    # doing this insanity so i dont have to use a for loop
    urls = list(map(lambda url: url.split("?")[0], sel.css("li.s-item a.s-item__link::attr(href)").getall()))
    
    urls = [url for url in urls if url != 'https://ebay.com/itm/123456'] # removes base urls

    return urls


# response = session.get("https://www.ebay.com/sch/i.html?&_nkw=shoe")


#response = session.get("https://www.ebay.com/sch/i.html?&_nkw=ungeuntary")
#response = session.get("https://www.ebay.com/sch/i.html?&_nkw=uninfluentiality")
#response = session.get("https://www.ebay.com/sch/i.html?&_nkw=plangent+figment")
#print(parse_search(response))

# https://www.ebay.com/sch/i.html?&_nkw=ungeuntary
# 
# response = session.get("https://www.ebay.com/sch/i.html?&_nkw=hat")
# scrape_search(response)

# response = session.get("https://www.ebay.com/sch/i.html?&_nkw=")
# print(parse_search(response))

def parse_search_list(url):
    response = session.get(f"{url}")
    search_data = parse_search(response)
    return search_data
