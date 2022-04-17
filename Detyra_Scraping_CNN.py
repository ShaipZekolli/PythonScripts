from bs4 import BeautifulSoup
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url = f'https://edition.cnn.com'
print("Faqja: "+ url +"\n")

s = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()
l = []

for link in soup.findAll('article', class_="cd cd--card cd--article cd--idx-0 cd--large cd--vertical cd--has-siblings cd--has-media cd--media__image cd--has-banner"):
            for a in link.findAll('a'):
                usl1 = "https://edition.cnn.com" + a.get('href')
                l.append(usl1)
                #print (a.get('href'))

for link in soup.findAll('article', class_="cd cd--card cd--article cd--idx-0 cd--large cd--vertical cd--has-siblings cd--has-media cd--media__image"):
            for a in link.findAll('a'):
                linku = a.get('href')
                if "https://" in linku:
                    usl = a.get('href')
                elif "http://" in linku:
                    usl = a.get('href')
                else:
                    usl = "https://edition.cnn.com" + a.get('href')
                l.append(usl)

def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

l2 =getUniqueItems(l)
#print(l[1])
for i in range(0,len(l2)):
#print(l)
    url2 = l2[i]
    code = requests.get(url2)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    title = s.find('h1').text
    print("Titulli         -->{"+title+"}")

    try:
        autori = s.find('span',class_='metadata__byline__author').text
        print("Shkruar nga     -->{"+autori+"}")
    except:
        try:
            autori2 = s.find('div',class_='Article__subtitle').text
            print("Shkruar nga     -->{"+autori2+"}")
        except:
            try:
                autori3 = s.find('span',class_='Authors__writer').text
                print("Shkruar nga     -->{"+ autori3+"}")
            except:
                print("Shkruar nga     -->{"+"Nuk ka te dhena}")

    try:
        koha = s.find('p',class_='update-time').text
        print("Koha e postimit -->{"+ koha+"}\n")
    except:
        try:
            koha2 =s.find('div', class_='PageHead__published').text
            print("Koha e postimit -->{"+ koha2+"}\n")
        except:
            print("Koha e postimit -->"+"{No data}\n")
    try:
        permbajtja = s.find('div',class_='l-container').text
        print("Permbajtja      -->{"+ permbajtja+"}\n")
    except:
        print("Permbajtja      -->{No data}\n")
print ("Artikujt e lajmeve të marra -->"+str(len(l2))+" artikuj")