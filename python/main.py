from search_scraper import parse_search_list
from page_scraper import * 
from words.return_words import *
from mongo_operations import db_add_product
#   from mongo_operations import display_db

if __name__ == "__main__":

    #   display_db()
    #   exit()
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
                try:
                    json_output = json.loads(output)    # turn product into json
                    response = db_add_product(json_output) # send json to db
                    if response == 0:
                        print("Product added to DB")
                        product_count += 1 # add to product count if successful
                    else:
                        print("Product failed to be added to DB")
                except Exception as e:
                    print(f"Error adding to db: {e}")
            #print(f"{output}")



        print(f"\nPRODUCT COUNT: {product_count}")
            
    print(f"\nFinal added product count: {product_count}")
        
