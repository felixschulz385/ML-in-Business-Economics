import re
import time
import json
import requests
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup

def main():
    # get the links
    links = pd.read_csv("nber_papers.csv").link
    
    # an element to store the data
    data = {}

    # iterate over the links
    for index, link in enumerate(tqdm(links)):
        
        # wait for decency
        time.sleep(.5)
        
        # get the page and turn into parsable soup
        try:
            soup = BeautifulSoup(requests.get("https://www.nber.org/" + link).content, 'html.parser')
        except:
            continue
        
        # initialize output dictionary
        out = {}
        
        try:
        
            # retrieve abstract
            out["abstract"] = soup.find("div", {"class": "page-header__intro-inner"}).get_text()
            
            # retrieve acknowledgements and disclosures
            out["a_d"] = soup.find("div", {"id": "accordion-body-guid1"}).p.get_text()
            
            # retrieve auxiliary links
            out["links"] = [x["href"] for x in soup.find_all("a", {"class": "link link--arrow"})]
            
            # retrieve DOI
            out["doi"] = re.sub("\nDOI |\n  ", "", soup.find_all("div", {"class": "page-header__citation-item"})[1].get_text())
            
            # retrieve associated topics and programs
            tmp = soup.find_all("div", {"class": "info-grid__item-body"})
            out["topics"] = tmp[0].find_all(text = True)
            out["programs"] = tmp[1].find_all(text = True)
            
        except:
            pass
        
        # write to list
        data[index] = out
            
        # save checkpoint
        if index % 10 == 0:
            with open("/home/ubuntu/ext_drive/HiWi/mlecon_scraping/ML-in-Business-Economics/nber_data_detailed.json", "w") as f:
                json.dump(data, f)


# run script
if __name__ == '__main__':
    main()