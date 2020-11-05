import typing
import requests
from bs4 import BeautifulSoup

pathname: str = 'https://www.lenovo.com/de/de/derewards/laptops/yoga/yoga-s-series/Lenovo-Yoga-S740-15IRH/p/88YGS701211'
cookies: str
headers: str

session = requests.session()
cookies = session.get()
headers = {}

response = session.get(pathname, headers=headers, cookies=cookies)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)
print('end')
print('end')
