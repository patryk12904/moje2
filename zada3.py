import random
slowa=("python","gdansk","dlaczego","gdynia","wsb")
word=random.choice(slowa)
#print(word)
poprawnie=word

pomie=""
while word:
	position = random.randrange(len(word))
	pomie+=word[position]
	word = word[:position]+word[(position+1):]
	#print(pomie)

print("""Witaj w grze Wymieszane litery Uporzadkuj litery 
aby odtworzyc prawidlowe slowo Aby zakonczyc zgadywanie nacisnij 
enter bez podawania odp""")
print("zgadnij jakie to slowo: ",pomie)
a=1
p=10
zgaduj = input("\nTwoja odpowiedz: ")
while zgaduj!=poprawnie and zgaduj != "":
	print("niestety to nie to slowo")
	if a>2:
		print("podpowiedz ")

		print(poprawnie[position:a-2])
	a+=1
	zgaduj=input("Twoja odpowiedz: ")

if zgaduj ==poprawnie:
	print("zgadza sie zgadles \n")
	print ("Twoje punkty: ", p-a)
		
print("dziekuje za udzial w grze")
