from urllib.request import urlopen
url="http://www.google.ca"
resp=urlopen(url)

print(resp.read())