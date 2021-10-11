from urllib.request import urlopen
url="http://www.google.com"
resp=urlopen(url)

print(resp.read())