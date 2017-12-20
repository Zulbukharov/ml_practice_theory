import urllib
from urllib.request import urlopen
import json


html = urlopen('http://185.22.64.26/others/?start')
s = html.read()
print(s)
ss = json.load(s)
print(ss)
