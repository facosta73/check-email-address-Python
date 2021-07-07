#check email address. primeras versiones

#de esta versión voy al siguiente archivo OKOK
#corrijo el doble @
#con el tipo jara.acosta@gmail.com.ar (aquí fallaría, porque hay 3 puntos, por tanto le digo a contador<4)
#corrijo el doble punto ".."


miemail=input("Introduzca su dirección de email: ")

cuenta_arroba=0
for a in miemail:
	if(a=="@"):
		cuenta_arroba=cuenta_arroba+1


contador_punto=0
for i in miemail:
	if(i=="."):
		contador_punto=contador_punto+1


if cuenta_arroba>1:
	print("email incorrecto")

elif ".." in miemail:
	print("mal")

elif contador_punto<3 and "@" in miemail and ".com" in miemail:   
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".es" in miemail:
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".org" in miemail:
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".eu" in miemail:
		print("el email es correcto")

elif contador_punto<4 and "@" in miemail and ".com.ar" in miemail: 
		print("el email es correcto")

else:
	print("email incorrecto")