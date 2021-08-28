import pandas as pd
import csv
import pickle
import re

tld_list = []
with open('results.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        tld_list.append(row[0])

pickle_in = open('terms.pickle', 'rb')
terms_list = pickle.load(pickle_in)


cleaned_terms = []
for x in terms_list:
    cleaned = re.sub(r'\W', '', x)
    cleaned = cleaned.lower()
    cleaned_terms.append(cleaned)


domains = []
for x in tld_list:
    for y in cleaned_terms:
        domain = y + x
        domains.append(domain)


pickle_out = open('domains.pickle', 'wb')
pickle.dump(domains, pickle_out)
pickle_out.close()