import requests
from bs4 import BeautifulSoup


def scrape_example():
    # url = "https://www.edunetfoundation.org/"
    # url = "https://www.google.com/"
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # title = soup.title.get_text()
        # print(f'Title of the Page:{title}')
        # print(soup.findAll("span"))
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            text = link.get_text()
            print(f"{text}: {href}")

    else:
        print(f"Failed")


scrape_example()
