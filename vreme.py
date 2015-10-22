
from bs4 import BeautifulSoup



url_str = 'http://www.pro-vreme.net/index.php?id=8'
import requests

r = requests.get(url_str).content

print([x.text for x in BeautifulSoup(r).find_all("table",attrs={"allign":"center"})])