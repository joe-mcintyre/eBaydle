from search_scraper import parse_search_list
from page_scraper import * 
from words.return_words import *

if __name__ == "__main__":
    product_count = 0

    while product_count < 1000:


        noun = get_rand_noun()
        adjective = get_rand_adjective()

        search_url = "https://www.ebay.com/sch/i.html?&_nkw=" + adjective +"+" + noun
        #print(f"{search_url}")

        url_list = parse_search_list(search_url)
        #print(f"{url_list}")

        for url in url_list:
            output = parse_product_json(f"{url}")
            if output not in ["list index out of range", "timeout", "error"]:
                product_count += 1
            #print(f"{output}")


        print(f"\nPRODUCT COUNT: {product_count}")
            
    print("\n\nDONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        
