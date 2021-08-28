import sys
import pickle
from tqdm import tqdm
from pprint import pprint
import whois as who


# pickle_in = open('domains.pickle', 'rb')
# domain_list = pickle.load(pickle_in)
#
# def whois_checker(domains):
#     avail = []
#     for x in tqdm(domains):
#         try:
#             check = whois(x)
#             if check.domain_name == None:
#                 sys.exit(1)
#         except:
#             avail.append(x)
#         else:
#             print(f'{x} is taken')
#     return avail

# invest = whois_checker(domain_list)
# print(invest)

def whois_check(domain):
    check = who.whois(domain)
    pass

test1 = who.whois('google.com')
test2 = who.whois('financewriter12.io')
test3 = who.whois('=.com')
test4 = who.whois('microsoft.com')
test5 = who.whois('fitz.city')
print(test1.get('domain_name'))
print(test2.get('domain_name'))
print(test5.get('domain_name'))
print(test4.get('domain_name'))









