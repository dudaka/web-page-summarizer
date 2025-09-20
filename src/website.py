import requests
from bs4 import BeautifulSoup

class Website:
    '''A utility class to represent a Website that we have scraped.'''
    def __init__(self, url: str):
        '''
        Create this Website object from the given url using the BeautifulSoup library.
        '''
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.title = soup.title.string if soup.title else 'No Title Found'
        for irrelevant in soup(['script', 'style', 'img', 'input']):
            irrelevant.decompose()
        self.text = soup.get_text(separator='\n', strip=True)

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Web_scraping'
    website = Website(url)
    print(f'Title: {website.title}\n')
    print(f'Content:\n{website.text[:500]}...')  # Print the first 500 characters of the text