from bs4 import BeautifulSoup
from lxml import html
import requests

import pandas as pd
from pytrends.request import TrendReq

from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import torch

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

pytrend = TrendReq()

test = soup.get_text("|", strip=True)

model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

nlp = pipeline('ner', model=model, tokenizer=tokenizer)

print(nlp(test))

words = nlp(test)

searchList = []
for i in words:
    print(i["word"])
    if (i["word"].find('#') != -1):
        if (i["score"] < .5):
            continue
        newstring = i["word"]
        searchList[-1] = searchList[-1] + newstring[1:]
    else:
        searchList.append(i["word"])

index = 0
trendsSearch = []

for i in searchList:
    if(index < 5):
        trendsSearch.append(i)
        index = index + 1
    else:
        print(pytrend.build_payload(trendsSearch))
        related_queries_dict = pytrend.related_queries()
        print(related_queries_dict)
        index = 0
        trendsSearch = []
