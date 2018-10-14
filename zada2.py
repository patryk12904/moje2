kom = input("Wprowadz komunikat")
kom1=len(kom)

print (kom[:: - 1])

for i in range (kom1,0,-1):
	print (kom[i-1])
