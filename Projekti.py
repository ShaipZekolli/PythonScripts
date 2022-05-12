#SHZ
import requests
import csv
import os

from tqdm import tqdm
from bs4 import BeautifulSoup

#Deklarimi i Variablave
pro = []
pro2 = []
em = []
pro1 = []
pro21 = []
em1 = []
print("[+] Duke u ekzekutuar", end="")
#Funksionet per marjen e presonelit te fakultetit
def web(page,WebUrl):

	if(page>0):

		url = WebUrl

		code = requests.get(url)

		plain = code.text
		s = BeautifulSoup(plain, "html.parser")
		global n, pro, pro2, em, d
		for link in s.findAll('div',class_="vc_custom_heading vc_gitem-post-data vc_gitem-post-data-source-post_title"):
			pro.append(link.text)
		for link in s.findAll('div',class_="vc_gitem-post-meta-field-Profesioni tituj vc_gitem-align-left"):
			pro2.append(" "+ link.text)
		for link in s.findAll('div',class_="vc_gitem-post-meta-field-Profesioni .tituj vc_gitem-align-left"):
			pro2.append(" "+ link.text)
		for link in s.findAll('div',class_="vc_gitem-post-meta-field-E-mail vc_gitem-align-left"):
			em.append(" "+link.text)

def web2(page1,WebUrl1):
		url1 = WebUrl1
		code1 = requests.get(url1)
		plain1 = code1.text
		s1 = BeautifulSoup(plain1, "html.parser")
		global pro1, pro21, em1, d1
		for link1 in s1.findAll('div',class_="vc_custom_heading vc_gitem-post-data vc_gitem-post-data-source-post_title"):
			pro1.append(link1.text)
		for link1 in s1.findAll('div',class_="vc_gitem-post-meta-field-Profesioni tituj vc_gitem-align-left"):
			pro21.append(" "+ link1.text)
		for link1 in s1.findAll('div',class_="vc_gitem-post-meta-field-Profesioni .tituj vc_gitem-align-left"):
			pro21.append(" "+ link1.text)
		for link1 in s1.findAll('div',class_="vc_gitem-post-meta-field-E-mail vc_gitem-align-left"):
			em1.append(" "+link1.text)
					
array = ['fshk','ekonomiku','juridiku','filologjia','fshjm','edukimi']	

for i in range(0 ,len(array)):
	if( i != ""):
		web(1,'https://'+ array[i] + '.uni-prizren.com/personeli-akademik/')
		print(".", end ="") 
	
for i in range(0 ,len(array)):
	if( i != ""):
		web2(1,'https://'+ array[i] + '.uni-prizren.com/personeli-administrativ/')
		print(".", end ="")
					
numritotal = "Numri Total: "+ str(len(pro))
header = ['Emri Mbiemri', 'Profesioni', 'E-Mail', numritotal]
d = []
for x in range(0,len(pro)):
	data = [
		pro[x], pro2[x], em[x],
	]
	d.append(data)

with open('personeli-akademik.xlsx', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	# write the header
	writer.writerow(header)
	# write multiple rows
	writer.writerows(d)
	print("\n[!] Fajlli i gjeneruar 'personeli-akademik.xlsx'")

numritotal1 = "Numri Total: "+ str(len(pro1))
header1 = ['Emri Mbiemri', 'Profesioni', 'E-Mail', numritotal1]
d1 = []
for x1 in range(0,len(pro1)):
	data1 = [
		pro1[x1], pro21[x1], em1[x1],
	]
	d1.append(data1)

with open('personeli-administrativ.xlsx', 'w', encoding='UTF8', newline='') as f1:
	writer = csv.writer(f1)
	# write the header
	writer.writerow(header1)
	# write multiple rows
	writer.writerows(d1)
	print("[!] Fajlli i gjeneruar 'personeli-administrativ.xlsx'\n")

code = requests.get("https://www.uni-prizren.com/upz/lajme/ngjarjet/")
plaintext = code.text

faqja = BeautifulSoup(plaintext, "html.parser")

links = []
for link in faqja.findAll('a',class_="vc_gitem-link"):
	links.append(link.get('href'))

links = list(set(links))
numriPosteve = len(links)

lajmet = []
for np in range(0,numriPosteve):
	urls = links[np]
	code1 = requests.get(urls)
	plaintext1 = code1.text

	faqja1 = BeautifulSoup(plaintext1, "html.parser")
	lajmet.append("Titulli    --> " + faqja1.find("h3").text)
	lajmet.append("Data       --> " + faqja1.find("time",class_="entry-date updated").text)
	lajmet.append("Permbajtaj --> " + faqja1.find("div",class_="uvc-sub-heading ult-responsive").text)
	lajmet.append("\n==================================================================================================================\n")

with open('ngjarjet-lajmet.txt', 'w') as filp:
	for element in lajmet:
		filp.write(element + "\n")
	print("[+] Fajlli i gjeneruar 'ngjarjet-lajmet.txt'")

#Historiku i Fakulteteve
fakultetet = []
for np1 in range(0,len(array)):
	
	code11 = requests.get('https://'+ array[np1] + '.uni-prizren.com/historiku-i-fakultetit/')
	plaintext11 = code11.text
	faqja11 = BeautifulSoup(plaintext11, "html.parser")

	code12 = requests.get('https://'+ array[np1] + '.uni-prizren.com/')
	plaintext12 = code12.text
	faqja12 = BeautifulSoup(plaintext12, "html.parser")

	fakultetet.append("Historku i " + faqja12.find("h3",class_="vc_custom_heading").text)
	try:
		fakultetet.append(faqja11.find("div",class_="wpb_text_column wpb_content_element").text)
	except:
		fakultetet.append("Nuk ka te dhena!")
	fakultetet.append("\n==================================================================================================================\n")

with open('historiku-i-fakulteteve.txt', 'w') as filpF:
	for elementF in fakultetet:
		filpF.write(elementF + "\n")
	print("[+] Fajlli i gjeneruar 'historiku-i-fakulteteve.txt'\n")


# CREATE FOLDER
def folder_create(images):
    try:
        folder_name = input(">> Emri i Folderit: ")
        os.mkdir(folder_name)

    # Nese folderi ekziston
    except:
        print("Folderi me kete emer ekziston!")
        folder_create()

    download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):

    count = 0
    noRep = set(images)
    print(f"Total {len(noRep)} Image Found!\n")

    if len(noRep) != 0:
        for item in tqdm(images):
            try:    
                r = requests.get(item["src"]).content
                imname = item["alt"]
                
                with open(f"{folder_name}/{imname}.jpg", "wb+") as f:
                    f.write(r)

                count += 1
            except:
                print("error")

        if count == len(images):
            print(f"[!] Imazhet mund ti gjeni ne folderin '{folder_name}'!")
            
        else:
            print(f"[!] Total {count} Images Downloaded Out of {len(noRep)}")

# MAIN FUNCTION START
def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.findAll('img', class_="vc_gitem-zone-img")
    folder_create(images)

#url = input("Enter URL:- ")

# MAIN FUNCTION
main("https://www.uni-prizren.com")
print("\n>> Finished")
