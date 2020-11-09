import requests
import re
from bs4 import BeautifulSoup

f = open(r"C:\Users\97\Desktop\yuanpeng.txt", "w")
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 '
               'Safari/537.36'}
pattern = re.compile('<div.class="ewb0info-a">.*?">"(.*?)"</a>.*?ewb-date">(.*?)</span>')
for i in range(1, 3):
    current_url = 'http://nxggzyjy.org/ningxiaweb/002/' + str(i) + '.html'
    html = requests.get(current_url, headers=headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    unit = soup.findAll("div", {"class": "ewb-info-a"})

    for item in unit:
        f.write(item.get_text())
        f.write("\n")
    for j in soup.find_all('a'):
        f.write(str((re.search(pattern, str(j)))))
f.close()
