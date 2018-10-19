import random
slowa=("python","gdansk","dlaczego","gdynia","wsb")
word=random.choice(slowa)
#print(word)
poprawnie=word
d=len(word)

print("""Witaj w grze. Program wylosuje slowo a ty musisz 
to slowo odgadnac. Masz 5 prob. Otrzymasz informacje tak lub nie czy
podana litera wystepuje w slowie.
Aby zakonczyc zgadywanie nacisnij 
enter bez podawania odp""")
i=0
while i<5 :
	print("\nzgadnij jakie to slowo,dlugosc slowa to: ",d)
	i+=1
	zgaduj = input("\nPodaj litere: ")
	if zgaduj =="":
		break
	if zgaduj in poprawnie :
		print("tak")
		print ("\npozostalo ci",5-i,"prob")
		
	else:
		print("nie")
		print ("pozostalo ci",5-i,"prob")
	if zgaduj == poprawnie:
		print ("\nzgadles!")
		break
if i==5:
	print ("\nnie udalo ci sie zgadnac")


		
print("\ndziekuje za udzial w grze")



