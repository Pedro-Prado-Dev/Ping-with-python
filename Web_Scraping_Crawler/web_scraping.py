from bs4 import BeautifulSoup
import requests


site = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site, 'html.parser')

# print(soup.prettify())

temp = soup.find("span", class_='-text')
print(temp)