#!/usr/bin/env python3
#-*- coding: utf-8-*-
odp=input("Jaka liczbe od 1 do 49 wylosowano ")
import random

liczba = random.randint(1,49)
print("Wylosowana liczba: ",liczba)
if liczba == int(odp):
	print("Hura!!")
else:
		print("No niestety")
