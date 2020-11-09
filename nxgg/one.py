import json
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import re


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<div.class="ewb0info-a">.*?">"(.*?)"</a>')
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '序号': item[0],
        }
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://nxggzyjy.org/ningxiaweb/002/21.html'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)