#SHZ
from bs4 import BeautifulSoup
import requests

headers = {
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}

response = requests.get('https://gjirafa50.com/', headers=headers)
html_page = response.text

soup = BeautifulSoup(html_page, "html.parser")

links = []
for link in soup.findAll('a'):
	links.append(link.get('href'))

internal = []
external = []
for link in links:
	try:
		if "https://gjirafa50.com/" in link:
			internal.append(link)
		else:
			external.append(link)
	except:
		pass
print("[+] Linqet externale:\n")
for ex in external:
	print(ex)

print("\n==============================================================================")
print("[+] Linqet internale:\n")
for inter in internal:
	print(inter)