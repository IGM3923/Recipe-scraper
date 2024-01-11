import requests 
from bs4 import BeautifulSoup
import pandas as pd

def build_scraper():
    offsets = [0, 24, 48, 72, 96, 120, 144, 168, 192, 216, 240, 
            264, 288, 312, 336, 360, 384, 408, 432, 456, 480, 
            504, 528, 552, 576, 600, 624, 648, 672, 696, 720]

    for offset in offsets:
        URL = f"https://www.allrecipes.com/search?vegan=vegan&offset={offset}&q=vegan"

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="search-results__content_1-0")
        elements = results.find_all(class_="comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")

        with open("test.txt", "a") as filename:
            for element in elements:
                # print(element, end="\n"*2, file=filename) # used to print entire search result for each element
                name = element.find(class_="card__title-text")
                typename = [item['data-tag'] for item in element.find_all(attrs={'data-tag' : True})]
                print(name.string + ',', typename[0] + ',', element.get('href') + ',', file=filename, end="\n")

        # search-results__content_1-0 is our search result div
        # comp mntl-card-list-items mntl-document-card mntl-card card card--no-image is our element div

def clean_scraper_results():
    # some cleaning is done manually
    # recategorize
    dessert_keywords = ['Brownie']
    df = pd.read_csv("test.csv")      
    print(df['meal'].drop_duplicates().to_list())

def main():
    clean_scraper_results()

if __name__ == "__main__":
    main()