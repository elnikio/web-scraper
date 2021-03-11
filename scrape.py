from urllib.request import urlopen
##from html.parser import HTMLParser
from bs4 import BeautifulSoup
html = urlopen('https://www.imdb.com/title/tt7939766/?ref_=fn_al_tt_1')
soup = BeautifulSoup(html, 'html.parser')
##print(soup.prettify())
print(type(soup))
print(soup.title)
print(soup.body.prettify()
