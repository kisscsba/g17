a=int(input("A haromszog elso oldala: "))
b=int(input("A haromszog masodik oldala: "))
c=int(input("A haromszog harmadik oldala: "))
if a+b> c and b+c>a and a+c>b:
	print("Ez a haromszog szerkeztheto")
else:
	print("Ez a haromszog nem szerkeztheto")
