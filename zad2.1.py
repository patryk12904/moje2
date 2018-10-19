import math
print ("Wprowadz oceny ,aby zakonczyc wpisywanie wcisnij 0")

przedmiot=input("Podaj przedmiot z ktorego chcesz policzyc oceny\n")
oceny=[]
ocena=1
while ocena!=0:
	try:
		ocena=int(input("Wprowadz ocene\n"))
		if (ocena >0 and ocena < 7):
			oceny.append(int(ocena))
		if ocena >6 and ocena < 0:
			print("nie ma takiej oceny!\n")
		
	except ValueError:
		print("bledne dane!\n")

print("Wprowadzone oceny:",oceny)
def srednia(oceny):
	suma=sum(oceny)
	return suma/float(len(oceny))
	
s=srednia(oceny)


def mediana(oceny):
	oceny.sort()
	h=int(len(oceny) /2)
	if len(oceny) % 2 == 0:
		
		return float((sum(oceny[h-1:h+1])) /2)
	else:
		
		return oceny[h]


		
def wariancja(oceny,srednia):
	sigma=0
	for ocena in oceny:
		sigma+=(ocena - srednia)**2
	return sigma/len(oceny)		
		
def odchylenie(oceny,srednia):
	w=wariancja(oceny,srednia)
	return math.sqrt(w)

print("wybrany przedmiot",przedmiot)
print("srednia to:",srednia(oceny))	
print("\nmediana to: ",mediana(oceny))
print("Odchylenie standardowe: ",odchylenie(oceny,s))

	

	

