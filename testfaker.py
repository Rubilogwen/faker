
from bs4 import BeautifulSoup
import  requests


url = 'https://dtf.ru/cinema'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
news = soup.find_all('div', class_ = 'content-title content-title--short l-island-a')
print(news)

for el in news:
    print(el.text).replace('\n' + ' ' * 36, ''))










