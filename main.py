import httpx
import json
from image_downloader import download_images
from page_scraper import parse_product

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

#   response = session.get("https://www.ebay.com/itm/332562282948")
#   product_data = parse_product(response)
#   print(json.dumps(product_data, indent=2))
#   
#   
#   response = session.get("https://www.ebay.com/itm/334520993657")
#   product_data = parse_product(response)
#   print(json.dumps(product_data, indent=2))
#   # response = session.get("https://www.ebay.com/p/10012") # want to inevitably switch to this url for scraping

# def ():

response = session.get("https://www.ebay.com/itm/204777023543")
product_data = parse_product(response)
#print(json.dumps(product_data, indent=2))

json_data = json.dumps(product_data)
# print(f"yo: {json_data}")

product_obj = json.loads(json_data)
product_photo_urls = [photo for photo in product_obj["photos"]]
download_images(product_photo_urls, session)

print("1")
response = session.get("https://www.ebay.com/itm/12314312413")
print("2")
product_data = parse_product(response)
print("3")
json_data = json.dumps(product_data)
print("4")
