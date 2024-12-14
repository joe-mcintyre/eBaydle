import os
from pathlib import Path
import httpx

def download_images(photo_urls, session, save_directory="images"):
    """
    Download images from a list of URLs and save them to a specified directory.

    Args:
        photo_urls (list): List of image URLs to download.
        session (httpx.Client): HTTPX session to use for requests.
        save_directory (str): Directory to save the downloaded images.
    """
    # make dir if doesnt exist
    os.makedirs(save_directory, exist_ok=True)
    # iter through image urls
    for index, url in enumerate(photo_urls, start=1):
        try:
            # Fetch the image data
            response = session.get(url)
            response.raise_for_status()  # quick error check
            
            # return file extension
            file_exten = url.split('.')[-1].split('?')[0]  # Handle cases with query parameters
            if file_exten not in ["jpg", "jpeg", "png", "webp"]:
                file_exten = "jpg"  # Default to jpg if the extension is unclear
            # print(url) # debug

            # shotty loop to make sure file doesnt override existing
            index2 = 0
            while True:
                index2 += 1
                file_name = file_name = f"{save_directory}/image_{index}_{index2}.{file_exten}"
                file_path = Path(file_name)
                if not file_path.exists():
                    break

            with open(file_name, "wb") as file: ## wb is writebinary, big brain
                file.write(response.content)
            
            print(f"img {index} saved as {file_name}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# Will remove below later, used for testing in single file
# Define the HTTPX session object
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

# Example usage with the photo URLs extracted from the JSON data
photo_urls = [
    "https://i.ebayimg.com/thumbs/images/g/B4UAAOSwMGhjGTg4/s-l500.jpg",
    "https://i.ebayimg.com/images/g/B4UAAOSwMGhjGTg4/s-l1600.webp"
]
download_images(photo_urls, session)
