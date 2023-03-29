import requests 
from bs4 import BeautifulSoup
url = "https://portfolio-wtdw.onrender.com/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)

