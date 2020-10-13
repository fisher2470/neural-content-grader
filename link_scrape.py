from bs4 import BeautifulSoup
from lxml import html
import requests

#save this url to be used later
page = input ("Enter url :")

#manipulate the string to find the domain name
domain = page[8:]
domain_length = len(page)

initial_url = page

page = requests.get(page)

page.text

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())

link_list = []

x=0
for link in soup.find_all('a'):
    x = x + 1
    print(link.get('href'))
    print("Link Number = ", x)
    link_list.append(link.get('href'))

total_links = x

internal_links = {}
outbound_links = {}

for link in link_list:
    try:
        if (link.find(domain)) != -1:
            if (link not in internal_links):
                print("Added ", link)
                internal_links[link] = 1
        else:
            outbound_links[link] = 1
    except AttributeError as el:
        print("Broken Link ", link)

check_list = []

check_list = list(internal_links.keys())

for link in check_list:
    if (link[0:1] == 'h'):
        new_url = link
        new_page = requests.get(new_url)
        new_page.text
        soup = BeautifulSoup(new_page.text, 'html.parser')
        print(soup.prettify())
        new_links = []
        for new_link in soup.find_all('a'):
            new_links.append(new_link.get('href'))
        for new_link in new_links:
            try:
                if (new_link in internal_links):
                    print("Included ", new_link)
                    count = internal_links[new_link]
                    internal_links[new_link] = count + 1
                elif (new_link != "") & (new_link.find(initial_url) != -1):
                    internal_links[new_link] = 1
                    check_list.append(new_link)
                    print("Added ", new_link)
                if (new_link != "") & (new_link.find(initial_url) == -1):
                    outbound_links[new_link] = 1
            except AttributeError as e:
                print("Dead Link ", new_link)
                continue #skips dead link

for link, count in internal_links.items():
    print("Internal Link: ", link)

f = open(domain + ".txt", "w+")
for link, count in internal_links.items():
    f.write("Internal Link: " + link + " is used: " + str(count) + " times\n")
for link, count in outbound_links.items():
    f.write("Outbound Link: " + link + " is used: " + str(count) + " times\n")
f.close

