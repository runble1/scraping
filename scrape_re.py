import re
from html import unescape

with open('dp.html') as f:
    html = f.read()

for partical_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    url = re.search(r'<a itemprop="url" href="(.*?)">', partical_html).group(1)
    url = 'https://gihyo.jp' + url

    title = re.search(r'<p itemprop="name".*?</p>', partical_html).group(0)
    title = title.replace('<br/>', ' ')
    title = re.sub(r'<.*?>', '', title)
    title = unescape(title)

    print(url, title)