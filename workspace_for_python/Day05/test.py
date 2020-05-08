import re
import requests

url = 'http://www.cnblogs.com/'

response = requests.get(url)
response.encoding = 'utf8'
html = response.text
print(type(html))
urls = re.findall('class=\"titlelnk\"\s*[^>]*?href=\"([^\"]+)', html)

for url in urls:
    print(url)

