import typing
import requests
from bs4 import BeautifulSoup

pathname: str = 'https://www.lenovo.com/de/de/derewards/laptops/yoga/yoga-s-series/Lenovo-Yoga-S740-15IRH/p/88YGS701211'
cookies: str
headers: str

session = requests.session()
cookies = session.get('https://www.lenovo.com/de/de/pc/')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

response = session.get(pathname, headers=headers, cookies=cookies)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)
