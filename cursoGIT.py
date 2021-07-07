#check email address. primeras versiones

contador=0
miemail=input("Introduzca su dirección de email: ")

for i in miemail:

	if(i=="@" or i=="."):
		contador=contador+1


if 1<contador<4 and "@" in miemail:
		print("el email es correcto")
else:
	print("email incorrecto")