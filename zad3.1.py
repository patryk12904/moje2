import math
a=int(input("Podaj dlugosc boku a "))
b=int(input("Podaj dlugosc boku b "))
c=int(input("Podaj dlugosc boku c "))

if a+b>c and b+c>a and a+c>b:
	print("\nDa sie zbudowac trojkat")
	print("Obwod wynosi ",a+b+c)
	p=((a+b+c)*0.5)
	s=math.sqrt(p*(p-a)*(p-b)*(p-c))
	print("Pole wynosi",s)
	if (a*a)+(b*b)==(c*c) or (b*b)+(c*c)==(a*a) or (a*a)+(c*c)==(b*b):
		print("\ntrojkat jest prostokatny ")
else:
	print(" nie da sie zbudowac trojkata ")
