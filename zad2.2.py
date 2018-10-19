import os
slownik = {}
sPlik = "slownik.txt"

def otworz(plik):
	if os.path.isfile(sPlik):
		with open(sPlik,"r") as pliktxt:
			for line in plitxt:
				t=line.split(":")
				wobcy=t[0]
				znaczenia=t[1].replace("\n","")
				znaczenia=znaczenia.split(",")
				slownik[wobcy]=znaczenia
	return len(slownik)
def zapisz(slownik):
	pliktxt=open(sPlik,"w")
	for wobcy in slownik:
		znaczenia= ",".join(slownik[wobcy])
		linia=":".join([wobcy,znaczenia])
		pliktxt.write(linia)
	pliktxt.close()
def oczysc(str):
	str=str.strip()
	str=str.lower()
	return str

print("""Podaj dane w formacie:
wyraz obcy:znaczenie1,znaczenie2. Aby zakonczyc wpisz koniec""")

nowy=False
ileWyrazow=otworz(sPlik)
print("Wpisow w bazie: ",ileWyrazow)

while True:
	dane=input("podaj dane: ")
	t=dane.split(":")
	wobcy=t[0].strip().lower()
	if wobcy == 'koniec':
		break
	elif dane.count(":") == 1 :
		if wobcy in slownik:
			print("Wyraz",wobcy,"juz sie znajduje")
			op=input("zastapic ?t/n")
		if wobcy not in slownik or op == "t":
			znaczenia = t[1].split(",")
			znaczenia=list(map(oczysc,znaczenia))
			slownik[wobcy]=znaczenia
			nowy=True
	else:
		print("Bledny format")
if nowy:
	zapisz(slownik)
print(slownik)
print("=" *50)
print("{0: <15}{1:<40}".format("Wyraz obcy","Znaczenia"))
print("=" *50)
for wobcy in slownik:
	print("{0: <15}{1:<40}".format(wobcy,",".join(slownik[wobcy])))
