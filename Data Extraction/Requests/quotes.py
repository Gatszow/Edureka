from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://quotes.toscrape.com/'
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
all_links = soup.find_all('div', {'class': 'quote'})
str_cells = str(all_links)
cleartext = BeautifulSoup(str_cells, 'lxml').get_text()

print(cleartext)
