from datetime import date
from bs4 import BeautifulSoup
import requests
from tinydb import TinyDB
 
today = str(date.today()).split('-')
year, month, day = [int(x) for x in today]

URL = 'https://www.brainyquote.com/quote_of_the_day'
db = TinyDB('./quotes.json')
response = requests.get(URL).text

soup = BeautifulSoup(response, 'html.parser')
funny = soup.find_all('h2')[-2]
funny_quote = funny.find_next('a').text.strip()
author = funny.find_next('a').find_next('a').text.strip()

db.insert({
    'day': day,
    'month': month,
    'year': year,
    'author': author,
    'quote': funny_quote
})
