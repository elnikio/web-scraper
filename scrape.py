from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
##from html.parser import HTMLParser
from bs4 import BeautifulSoup

# exception handling :
try:
    html = urlopen('https://www.imdb.com/title/tt7939766/?ref_=fn_al_tt_1')

except HTTPError as hrr:
    # hrr is just an alias for HTTPError
    print(hrr)
    print("Page not found.")

except URLError as urr:
    # urr is just an alias for URLError
    print(urr)
    print("Server not found.")

else:
    print("HTTP and and Server found!")
    
    soup = BeautifulSoup(html, 'html.parser')
    ##print(soup.prettify())
    print(type(soup))
    print(soup.find('a').find('href'))
    #print("tag a:",soup.a['href'])
    ##print(soup.body.prettify())
