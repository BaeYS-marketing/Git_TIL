import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(response, 'html.parser')

kospi = soup.select_one('#KOSPI_now')
#print(kospi.text)



practice = requests.get("https://finance.naver.com/marketindex/").text

p_soup = BeautifulSoup(practice,"html.parser")

p_kospi = p_soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(p_kospi.text)