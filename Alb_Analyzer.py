#Sh Z
import tkinter as tk
from tkinter import * 
import PyPDF2
from tkinter.filedialog import askopenfile
import re
from collections import Counter

def open_file():
	browse_text.set("Procesim...")
	file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
	if file:
		text=""
		read_pdf = PyPDF2.PdfFileReader(file)
		for x in reversed(range(0,read_pdf.numPages)):
			page = read_pdf.getPage(x)
			page_content = page.extractText()
			#text box
			tInput.insert(1.0, page_content)
			
		browse_text.set("Ngarko PDF")

def PerseritjaKaraktereve():
	tekstPrejInput = tInput.get(1.0, "end-1c")
	count1 = Counter(tekstPrejInput)

	stringKaraktere = (
	" 1--> " + str(count1['1']) +
	"\n 2--> " + str(count1['2']) +
	"\n 3--> " + str(count1['3']) +
	"\n 4--> " + str(count1['4']) +
	"\n 5--> " + str(count1['5']) +
	"\n 6--> " + str(count1['6']) +
	"\n 7--> " + str(count1['7']) +
	"\n 8--> " + str(count1['8']) +
	"\n 9--> " + str(count1['9']) +
	"\n 0--> " + str(count1['0']) +
	"\n\nHapsira: " + str(count1[' ']) +
	"\n\n ;--> " + str(count1[';'])   +
	"\n .--> " + str(count1['.'])   +
	"\n ,--> " + str(count1[','])   +
	"\n /--> " + str(count1['/'])   +
	"\n !--> " + str(count1['!'])   +
	"\n @--> " + str(count1['@'])   +
	"\n %--> " + str(count1['%'])   +
	"\n &--> " + str(count1['&'])   +
	"\n *--> " + str(count1['*'])   +
	"\n (--> " + str(count1['('])   +
	"\n :--> " + str(count1[':'])   +
	"\n +--> " + str(count1['+'])   +
	"\n =--> " + str(count1['='])   +
	"\n ?--> " + str(count1['?'])   +
	"\n #--> " + str(count1['#'])   +
	"\n )--> " + str(count1[')'])
	)
	return stringKaraktere 


def PerseritjaShkronjave():
	tekstPrejInput = tInput.get(1.0, "end-1c")
	count = Counter(tekstPrejInput)

#Per shkronjat e vogla
	nrdh = tekstPrejInput.count('dh')
	nrgj = tekstPrejInput.count('gj')
	nrll = tekstPrejInput.count('ll')
	nrnj = tekstPrejInput.count('nj')
	nrrr = tekstPrejInput.count('rr')
	nrsh = tekstPrejInput.count('sh')
	nrth = tekstPrejInput.count('th')
	nrxh = tekstPrejInput.count('xh')
	nrzh = tekstPrejInput.count('zh')

#Per shkronjat e medha
	nrDh = tekstPrejInput.count('Dh')
	nrGj = tekstPrejInput.count('Gj')
	nrLl = tekstPrejInput.count('Ll')
	nrNj = tekstPrejInput.count('Nj')
	nrRr = tekstPrejInput.count('Rr')
	nrSh = tekstPrejInput.count('Sh')
	nrTh = tekstPrejInput.count('Th')
	nrXh = tekstPrejInput.count('Xh')
	nrZh = tekstPrejInput.count('Zh')

	global NumriDyshkronjave
	NumriDyshkronjave = nrdh + nrgj + nrll + nrnj + nrrr + nrsh + nrth + nrxh + nrzh + nrDh + nrGj + nrLl + nrNj + nrRr + nrSh + nrTh + nrXh + nrZh
	stringUp =""

	textPaHapsira = tekstPrejInput.replace(" ","")
	numriKaraktereve = len(textPaHapsira)
	stringUp=""
	if numriKaraktereve != 0:
		stringUp = (
		" A--> " + str(count['A']) +					"		a--> " + str(count['a']) +
		"\n B--> " + str(count['B']) +					"		b--> " + str(count['b']) +
		"\n C--> " + str(count['C']) +					"		c--> " + str(count['c']) +
		"\n Ç--> " + str(count['Ç'])  +					"		ç--> " + str(count['ç']) +
		"\n D--> " + str(count['D']-nrDh) +				"		d--> " + str(count['d']-nrdh) +
		"\n Dh-> " + str(tekstPrejInput.count('Dh')) + 	"		dh-> " + str(tekstPrejInput.count('dh')) +
		"\n E--> " + str(count['E']) +					"		e--> " + str(count['e']) +
		"\n Ë--> " + str(count['Ë']) +					"		ë--> " + str(count['ë']) +
		"\n F--> " + str(count['F']) +					"		f--> " + str(count['f']) +
		"\n G--> " + str(count['G']-nrGj) +				"		g--> " + str(count['g']-nrgj) +
		"\n Gj-> " + str(tekstPrejInput.count('Gj')) + 	"		gj-> " + str(tekstPrejInput.count('gj')) +
		"\n H--> " + str(count['H']) +					"		h--> " + str(count['h']-nrdh-nrsh-nrxh-nrzh-nrth-nrDh-nrSh-nrXh-nrZh-nrTh) +
		"\n I--> " + str(count['I']) +					"		i--> " + str(count['i']) +
		"\n J--> " + str(count['J']) +					"		j--> " + str(count['j']-nrgj-nrnj-nrGj-nrNj) +
		"\n K--> " + str(count['K']) +					"		k--> " + str(count['k']) +
		"\n L--> " + str(count['L']-nrLl) +				"		l--> " + str(count['l']- (2*nrll)-nrLl) +
		"\n Ll-> " + str(tekstPrejInput.count('Ll')) + 	"		ll-> " + str(tekstPrejInput.count('ll')) +
		"\n M--> " + str(count['M']) +					"		m--> " + str(count['m']) +
		"\n N--> " + str(count['N']-nrNj) +				"		n--> " + str(count['n']-nrnj) +
		"\n Nj-> " + str(tekstPrejInput.count('Nj')) + 	"		nj-> " + str(tekstPrejInput.count('nj')) +
		"\n O--> " + str(count['O']) +					"		o--> " + str(count['o']) +
		"\n P--> " + str(count['P']) +					"		p--> " + str(count['p']) +
		"\n Q--> " + str(count['Q']) +					"		q--> " + str(count['q']) +
		"\n R--> " + str(count['R']-nrRr) +				"		r--> " + str(count['r']-(2*nrrr)-nrRr) +
		"\n Rr-> " + str(tekstPrejInput.count('Rr')) + 	"		rr-> " + str(tekstPrejInput.count('rr')) +
		"\n S--> " + str(count['S']-nrSh) +				"		s--> " + str(count['s']-nrsh) +
		"\n Sh-> " + str(tekstPrejInput.count('Sh')) + 	"		sh-> " + str(tekstPrejInput.count('sh')) +	
		"\n T--> " + str(count['T']-nrTh) +				"		t--> " + str(count['t'] -nrth) +
		"\n Th-> " + str(tekstPrejInput.count('Th')) + 	"		th-> " + str(tekstPrejInput.count('th')) +
		"\n U--> " + str(count['U']) +					"		u--> " + str(count['u']) +
		"\n V--> " + str(count['V']) +					"		v--> " + str(count['v']) +
		"\n X--> " + str(count['X']-nrXh) +				"		x--> " + str(count['x']-nrxh) +
		"\n Xh-> " + str(tekstPrejInput.count('Xh')) + 	"		xh-> " + str(tekstPrejInput.count('xh')) +
		"\n Y--> " + str(count['Y']) +					"		y--> " + str(count['y']) +
		"\n Z--> " + str(count['Z']-nrZh) +				"		z--> " + str(count['z']-nrzh) +
		"\n Zh-> " + str(tekstPrejInput.count('Zh')) + 	"		zh-> " + str(tekstPrejInput.count('zh'))
		)
	return stringUp

def FrekuencaSh():
	tekstPrejInput = tInput.get(1.0, "end-1c")
	count = Counter(tekstPrejInput)

#Per shkronjat e vogla
	nrdh = tekstPrejInput.count('dh')
	nrgj = tekstPrejInput.count('gj')
	nrll = tekstPrejInput.count('ll')
	nrnj = tekstPrejInput.count('nj')
	nrrr = tekstPrejInput.count('rr')
	nrsh = tekstPrejInput.count('sh')
	nrth = tekstPrejInput.count('th')
	nrxh = tekstPrejInput.count('xh')
	nrzh = tekstPrejInput.count('zh')

#Per shkronjat e medha
	nrDh = tekstPrejInput.count('Dh')
	nrGj = tekstPrejInput.count('Gj')
	nrLl = tekstPrejInput.count('Ll')
	nrNj = tekstPrejInput.count('Nj')
	nrRr = tekstPrejInput.count('Rr')
	nrSh = tekstPrejInput.count('Sh')
	nrTh = tekstPrejInput.count('Th')
	nrXh = tekstPrejInput.count('Xh')
	nrZh = tekstPrejInput.count('Zh')

#Numri total i karaktereve
	textPaHapsira = tekstPrejInput.replace(" ","")
	numriKaraktereve = len(textPaHapsira)
	stringFrekuenca=""
	if numriKaraktereve != 0:
		stringFrekuenca = (
		" A ~ " + str(round(count['A']/numriKaraktereve*100,2))+"%" +					"		a ~ " + str(round(count['a']/numriKaraktereve*100,2))+"%" +
		"\n B ~ " + str(round(count['B']/numriKaraktereve*100,2))+"%" +					"		b ~ " + str(round(count['b']/numriKaraktereve*100,2))+"%" +
		"\n C ~ " + str(round(count['C']/numriKaraktereve*100,2))+"%" +					"		c ~ " + str(round(count['c']/numriKaraktereve*100,2))+"%" +
		"\n Ç ~ " + str(round(count['Ç']/numriKaraktereve*100,2))+"%" +					"		ç ~ " + str(round(count['ç']/numriKaraktereve*100,2))+"%" +
		"\n D ~ " + str(round((count['D']-nrDh)/numriKaraktereve*100,2))+"%"+			"		d ~ " + str(round((count['d']-nrdh)/numriKaraktereve*100,2))+"%"+
		"\n Dh- " + str(round(tekstPrejInput.count('Dh')/numriKaraktereve*100,2))+"%"+ 	"		dh- " + str(round(tekstPrejInput.count('dh')/numriKaraktereve*100,2))+"%"+
		"\n E ~ " + str(round(count['E']/numriKaraktereve*100,2))+"%" +					"		e ~ " + str(round(count['e']/numriKaraktereve*100,2))+"%" +
		"\n Ë ~ " + str(round(count['Ë']/numriKaraktereve*100,2))+"%" +					"		ë ~ " + str(round(count['ë']/numriKaraktereve*100,2))+"%" +
		"\n F ~ " + str(round(count['F']/numriKaraktereve*100,2))+"%" +					"		f ~ " + str(round(count['f']/numriKaraktereve*100,2))+"%" +
		"\n G ~ " + str(round((count['G']-nrGj)/numriKaraktereve*100,2))+"%" +			"		g ~ " + str(round((count['g']-nrgj)/numriKaraktereve*100,2))+"%" +
		"\n Gj- " + str(round(tekstPrejInput.count('Gj')/numriKaraktereve*100,2))+"%"+ 	"		gj- " + str(round(tekstPrejInput.count('gj')/numriKaraktereve*100,2))+"%"+
		"\n H ~ " + str(round(count['H']/numriKaraktereve*100,2))+"%" +					"		h ~ " + str(round((count['h']-nrdh-nrsh-nrxh-nrzh-nrth-nrDh-nrSh-nrXh-nrZh-nrTh)/numriKaraktereve*100,2))+"%"+
		"\n I ~ " + str(round(count['I']/numriKaraktereve*100,2))+"%" +					"		i ~ " + str(round(count['i']/numriKaraktereve*100,2))+"%" +
		"\n J ~ " + str(round(count['J']/numriKaraktereve*100,2))+"%" +					"		j ~ " + str(round((count['j']-nrgj-nrnj-nrGj-nrNj)/numriKaraktereve*100,2))+"%"+
		"\n K ~ " + str(round(count['K']/numriKaraktereve*100,2))+"%" +					"		k ~ " + str(round(count['k']/numriKaraktereve*100,2))+"%" +	
		"\n L ~ " + str(round((count['L']-nrLl)/numriKaraktereve*100,2))+"%" +			"		l ~ " + str(round((count['l']- (2*nrll)-nrLl)/numriKaraktereve*100,2))+"%"+
		"\n Ll- " + str(round(tekstPrejInput.count('Ll')/numriKaraktereve*100,2))+"%"+ 	"		ll- " + str(round(tekstPrejInput.count('ll')/numriKaraktereve*100,2))+"%"+
		"\n M ~ " + str(round(count['M']/numriKaraktereve*100,2))+"%" +					"		m ~ " + str(round(count['m']/numriKaraktereve*100,2))+"%"+
		"\n N ~ " + str(round((count['N']-nrNj)/numriKaraktereve*100,2))+"%" +			"		n ~ " + str(round((count['n']-nrnj)/numriKaraktereve*100,2))+"%"+
		"\n Nj- " + str(round(tekstPrejInput.count('Nj')/numriKaraktereve*100,2))+"%"+	"		nj- " + str(round(tekstPrejInput.count('nj')/numriKaraktereve*100,2))+"%"+
		"\n O ~ " + str(round(count['O']/numriKaraktereve*100,2))+"%" +					"		o ~ " + str(round(count['o']/numriKaraktereve*100,2))+"%" +
		"\n P ~ " + str(round(count['P']/numriKaraktereve*100,2))+"%" +					"		p ~ " + str(round(count['p']/numriKaraktereve*100,2))+"%" +
		"\n Q ~ " + str(round(count['Q']/numriKaraktereve*100,2))+"%" +					"		q ~ " + str(round(count['q']/numriKaraktereve*100,2))+"%" +
		"\n R ~ " + str(round((count['R']-nrRr)/numriKaraktereve*100,2))+"%"+			"		r ~ " + str(round((count['r']-(2*nrrr)-nrRr)/numriKaraktereve*100,2))+"%"+
		"\n Rr- " + str(round(tekstPrejInput.count('Rr')/numriKaraktereve*100,2))+"%"+ 	"		rr- " + str(round(tekstPrejInput.count('rr')/numriKaraktereve*100,2))+"%"+
		"\n S ~ " + str(round((count['S']-nrSh)/numriKaraktereve*100,2))+"%"+			"		s ~ " + str(round((count['s']-nrsh)/numriKaraktereve*100,2))+"%"+
		"\n Sh- " + str(round(tekstPrejInput.count('Sh')/numriKaraktereve*100,2))+"%"+ 	"		sh- " + str(round(tekstPrejInput.count('sh')/numriKaraktereve*100,2))+"%"+	
		"\n T ~ " + str(round((count['T']-nrTh)/numriKaraktereve*100,2))+"%"+			"		t ~ " + str(round((count['t'] -nrth)/numriKaraktereve*100,2))+"%"+
		"\n Th- " + str(round(tekstPrejInput.count('Th')/numriKaraktereve*100,2))+"%"+ 	"		th- " + str(round(tekstPrejInput.count('th')/numriKaraktereve*100,2))+"%"+
		"\n U ~ " + str(round(count['U']/numriKaraktereve*100,2))+"%"+					"		u ~ " + str(round(count['u']/numriKaraktereve*100,2))+"%"+
		"\n V ~ " + str(round(count['V']/numriKaraktereve*100,2))+"%"+					"		v ~ " + str(round(count['v']/numriKaraktereve*100,2))+"%"+
		"\n X ~ " + str(round((count['X']-nrXh)/numriKaraktereve*100,2))+"%"+			"		x ~ " + str(round((count['x']-nrxh)/numriKaraktereve*100,2))+"%"+
		"\n Xh- " + str(round(tekstPrejInput.count('Xh')/numriKaraktereve*100,2))+"%"+	"		xh- " + str(round(tekstPrejInput.count('xh')/numriKaraktereve*100,2))+"%"+
		"\n Y ~ " + str(round(count['Y']/numriKaraktereve*100,2))+"%"+					"		y ~ " + str(round(count['y']/numriKaraktereve*100,2))+"%"+
		"\n Z ~ " + str(round((count['Z']-nrZh)/numriKaraktereve*100,2))+"%"+			"		z ~ " + str(round((count['z']-nrzh)/numriKaraktereve*100,2))+"%"+
		"\n Zh- " + str(round(tekstPrejInput.count('Zh')/numriKaraktereve*100,2))+"%"+	"		zh- " + str(round(tekstPrejInput.count('zh')/numriKaraktereve*100,2))+"%"
		)
	return stringFrekuenca

def analizo():
	textout.configure(state='normal')
	textout.delete('1.0', END)
	stringSH = PerseritjaShkronjave()
	tekstPrejInput = tInput.get(1.0, "end-1c")
	textout.insert(1.0,stringSH)#pd.Series(list(tekstPrejInput)).value_counts()
	textout.configure(state='disabled')

	textouttt.configure(state='normal')
	textouttt.delete('1.0', END)
	stringK = PerseritjaKaraktereve()
	textouttt.insert(1.0,stringK)
	textouttt.configure(state='disabled')


	textFrekuenca.configure(state='normal')
	textFrekuenca.delete('1.0', END)
	stringF = FrekuencaSh()
	textFrekuenca.insert(1.0,stringF)
	textFrekuenca.configure(state='disabled')

	tInputtt.configure(state='normal')
	tInputtt.delete('1.0', END)

	textPaHapsira = tekstPrejInput.replace(" ","")
	tInputtt.insert(1.0,"Numri i Karaktereve:" + str(len(textPaHapsira) ))
	tInputtt.insert(1.0,"Numri i Fjaleve: " + str(len(re.findall(r'\w+', tekstPrejInput))) + "\n")
	tInputtt.insert(1.0,"Numri i Dyshkronjave: " + str(NumriDyshkronjave) + "\n")
	tInputtt.configure(state='disabled')

root = Tk()

# This is the section of code which creates the main window
root.geometry('1200x650')
root.configure(background='#F0F8FF')
root.title('Alb_Analayzer')



# This is the section of code which creates the a label
Label(root, text='Jepni tekstin per ta analizuar:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=100, y=37)

browse_text = tk.StringVar()
browse_text.set("Ngarko PDF")
# This is the section of code which creates a button
Button(root, text='Analizo', bg='#F0F8FF', font=('arial', 12, 'normal'), command=lambda:analizo()).place(x=320, y=34)



# This is the section of code which creates a button
Button(root, text='Ngarko PDF', textvariable=browse_text,bg='#F0F8FF', font=('arial', 12, 'normal'), command=lambda:open_file()).place(x=410, y=34)


# This is the section of code which creates a text input box
tInput=Text(root)
tInput.place(x=29, y=105, height=520, width=520)


# This is the section of code which creates a text input box
Label(root, text='Perseritja e Shkronjave:', bg='#F0F8FF', font=('arial', 10, 'normal')).place(x=580, y=38)
textout=Text(root)
textout.place(x=580, y=55 ,height=500, width=250)
textout.configure(state='disabled')

#Frekuenca tekstit
Label(root, text='Frekuenca e Shkronjave:', bg='#F0F8FF', font=('arial', 10, 'normal')).place(x=840, y=38)
textFrekuenca=Text(root)
textFrekuenca.place(x=840, y=55 ,height=500, width=220)
textFrekuenca.configure(state='disabled')

# This is the section of code which creates a text input box
Label(root, text='Karakteret:', bg='#F0F8FF', font=('arial', 10, 'normal')).place(x=1070, y=38)
textouttt=Text(root)
textouttt.place(x=1070, y=55 ,height=500, width=100)
textouttt.configure(state='disabled')

# This is the section of code which creates a text input box
tInputtt=Text(root)
tInputtt.place(x=580, y=560 , height=80, width=480)
tInputtt.configure(state='disabled')

canvas = Canvas(root, width = 100, height = 100, bd=0, highlightthickness=0, relief='ridge')
	  
canvas.pack(side=TOP, anchor=NW)      
img = PhotoImage(file="Universiteti_i_Prizrenit.png")      
canvas.create_image(0,0, anchor=NW, image=img)
canvas.configure(bg='#F0F8FF')
root.iconphoto(False, img)

root.mainloop()
