from bs4 import BeautifulSoup

import requests

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
print(title_list)

for idx, title in enumerate(title_list, 1):
    print(idx, title.text)