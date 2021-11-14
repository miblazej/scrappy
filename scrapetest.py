from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h1
  except AttributeError as e:
    return None
  return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
  print('Tytuł nie został znaleziony')
else: 
  print(title)