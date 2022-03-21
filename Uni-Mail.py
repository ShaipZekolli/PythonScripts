import requests

from bs4 import BeautifulSoup

def web(page,WebUrl):

	if(page>0):

		url = WebUrl

		code = requests.get(url)

		plain = code.text

		s = BeautifulSoup(plain, "html.parser")
		for link in s.findAll('div',class_="vc_gitem-post-meta-field-E-mail vc_gitem-align-left"):
			for a in link.findAll('a'):
				print (a.text)

while(True):
    print ("""
    1.Fshk
    2.Ekonomik
    3.Juridik
    4.Filofogji
    5.Fshjm
    6.Edukimit
    7.Te gjitha
    """)
    ans=input("Zgjedh njerin nga departamentet? ")

    print("__________________________________\n") 
    if ans=="1": 
        web(1,'https://fshk.uni-prizren.com/personeli-akademik/')
        print("__________________________________\n") 
    elif ans=="2":
        web(1,'https://ekonomiku.uni-prizren.com/personeli-akademik/')
        print("__________________________________\n") 
    elif ans=="3":
        web(1,'https://juridiku.uni-prizren.com/personeli-akademik/')
        print("__________________________________\n") 
    elif ans=="4":
        web(1,'https://filologjia.uni-prizren.com/personeli-akademik/')
        print("__________________________________\n") 
    elif ans=="5":
        web(1,'https://fshjm.uni-prizren.com/personeli-akademik/')
        print("__________________________________\n") 
    elif ans=="6":
        web(1,'https://edukimi.uni-prizren.com/personeli-akademik/')
        print("__________________________________\n") 
    elif ans !="":
        web(1,'https://uni-prizren.com/personeli-akademik/') 
        print("End __________________________________\n") 

    array = ['fshk','ekonomiku','juridiku','filologjia','fshjm','edukimi']
    if ans=="7":	
        for i in range(0 ,len(array)):
                if( i != ""):
                    web(1,'https://'+ array[i] + '.uni-prizren.com/personeli-akademik/')
                    print("__________________________________\n") 
                    i = i + 1

#web(1,'https://fshk.uni-prizren.com/personeli-akademik/')