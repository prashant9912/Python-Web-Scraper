import requests
from  bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(page.status_code)
   
print(page.content)


soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

print(soup.find_all('p')[0].get_text())