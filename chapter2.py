from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'lxml')
for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
  print(sibling)

# html1 = urlopen('https://www.onet.pl')
# bs_wp = BeautifulSoup(html1.read(),'lxml')
# h1_list= bs_wp.findAll('h1')
# for h1 in h1_list:
#   print(h1.get_text())