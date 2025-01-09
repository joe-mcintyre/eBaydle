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
    follow_redirects=True,
    timeout=10
)

def parse_product(response: httpx.Response) -> dict:
    """
    Scrapes a product's core data from a ebay url by selecting important html sections.
    Returns item library with all related data.

    Args:
        response: httpx response from an exterior http session object
    """
    sel = Selector(response.text)
    # helper functions 
    css_join = lambda css: "".join(sel.css(css).getall()).strip()  # join all selected elements
    css = lambda css: sel.css(css).get("").strip()  # take first selected element and strip of leading/trailing spaces

    item = {}
    item["url"] = css('link[rel="canonical"]::attr(href)')
    item["id"] = item["url"].split("/itm/")[1].split("?")[0]  # grab id from url
    item["name"] = css(".x-item-title__mainTitle>span::text")
    item["price_original"] = css(".x-price-primary>span::text")
    item["price_converted"] = css(".-price-approx__price ::text")
    item["seller_name"] = sel.xpath("//div[contains(@class,'info__about-seller')]/a/span/text()").get()
    item["seller_url"] = sel.xpath("//div[contains(@class,'info__about-seller')]/a/@href").get().split("?")[0]
    item["photos"] = sel.css('.ux-image-filmstrip-carousel-item.image img::attr("src")').getall()  # carousel images
    item["photos"].extend(sel.css('.ux-image-carousel-item.image img::attr("src")').getall())  # main image
    item["photos"].extend(sel.css('.ux-image-grid-item img::attr(src)').getall())  # extra images

    item["photos"] = list(set(item["photos"])) # Remove dups

    # description is iframe independant page, can keep as URL or scrape it later?
    item["description_url"] = css("iframe#desc_ifr::attr(src)")
    
    # feature details from the description table:
    features = {}
    feature_table = sel.css("div.ux-layout-section--features")
    for feature in feature_table.css("dl.ux-labels-values"):
        # iterate through each label of the table and select first sibling for value:
        label = "".join(feature.css(".ux-labels-values__labels-content > div > span::text").getall()).strip(":\n ")
        value = "".join(feature.css(".ux-labels-values__values-content > div > span *::text").getall()).strip(":\n ")
        features[label] = value
    item["features"] = features

    return item

def parse_product_json(url):
    try:
        response = session.get(f"{url}")
        product_data = parse_product(response)
        return json.dumps(product_data, indent=2) # probably remove indent later
    except httpx.ReadTimeout:
        print(f"Timeout occurred on URL: {url}")
        return "timeout"
    except IndexError as i_error:
        return str(i_error)
    except Exception as e:
        print(f"error occurred on URL: {url}, {str(e)}")
        return "error"

"""
try:
    response = session.get("https://www.ebay.com/itm/286249399022")
    product_data = parse_product(response) 
    print(json.dumps(product_data, indent=2))
except IndexError:
    print("invalid url index")
"""

"""
# example usage
response = session.get("https://www.ebay.com/itm/332562282948")
product_data = parse_product(response)
print(json.dumps(product_data, indent=2))


try:
    response = session.get("https://www.ebay.com/itm/1239034")
    product_data = parse_product(response) 
    print(json.dumps(product_data, indent=2))
except IndexError:
    print("invalid url index")

try:
    response = session.get("https://www.ebay.com/sch/i.html?&_nkw=shoe")
    product_data = parse_product(response) 
    print(json.dumps(product_data, indent=2))
except IndexError:
    print("invalid url index")
"""
