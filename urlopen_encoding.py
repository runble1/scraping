import sys
from urllib.request import urlopen

f = urlopen('https://gihyo.jp/dp')

# HTTPヘッダーからエンコーディングを取得する（明示されていない場合はutf-8）
encoding = f.info().get_content_charset(failobj="utf-8")

# 標準エラー出力に出力
print('encoding:', encoding, file=sys.stderr)

text = f.read().decode(encoding)
print(text)
