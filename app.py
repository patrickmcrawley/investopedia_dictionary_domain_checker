from bs4 import BeautifulSoup
import re
import requests
import pickle

url = requests.get('https://www.investopedia.com/financial-term-dictionary-4769738')
soup = BeautifulSoup(url.content, 'lxml')
term_links = soup.findAll('a', text=re.compile('See complete list of'))

stripped_links = []

for x in term_links:
    link = x.get('href')
    stripped_links.append(link)

term_list = []
for x in stripped_links:
    url = requests.get(x)
    soup = BeautifulSoup(url.content, 'lxml')
    links = soup.find('main', {"class": "comp dictionary-listing mntl-block"})
    linktext = links.findAll('a')
    for y in linktext:
        term = y.text
        term_list.append(term)

print(term_list)


pickle_out = open("terms.pickle", 'wb')
pickle.dump(term_list, pickle_out)
pickle_out.close()