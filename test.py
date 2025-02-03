# import requests
# from bs4 import BeautifulSoup

# def simple_crawler(url):
#     # Send a request to the website
#     response = requests.get(url)
    
#     # Check if request was successful
#     if response.status_code != 200:
#         print("Failed to retrieve the webpage")
#         return
    
#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Extract and print all links on the page
#     for link in soup.find_all('a'):
#         href = link.get('href')
#         if href:
#             print(href)

# # Example usage
# simple_crawler('https://edunetfoundation.org/')


import requests
from bs4 import BeautifulSoup

def web_crawler(start_url, max_pages=20): 
    visited = set()
    to_visit = [start_url]
    
    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        
        print(f"Crawling: {url}")
        visited.add(url)
        
        try:
            response = requests.get(url)
            if response.status_code != 200:
                continue
        except requests.RequestException:
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href.startswith('http') and href not in visited:
                to_visit.append(href)

# Example usage
web_crawler('https://edunetfoundation.org/')
