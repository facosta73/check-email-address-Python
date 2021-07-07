#check email address. primeras versiones

miemail=input("Introduzca su dirección de email: ")

cuenta_arroba=0
for a in miemail:
	if(a=="@"):
		cuenta_arroba=cuenta_arroba+1


contador_punto=0
for i in miemail:
	if(i=="."):
		contador_punto=contador_punto+1

contador_guion=0
for g in miemail:
	if(g=="_"):
		contador_guion=contador_guion+1


if cuenta_arroba>1:
	print("email incorrecto")

if contador_punto<3 and "@" in miemail and ".com" in miemail and contador_guion<2:   
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".es" in miemail and contador_guion<2:
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".org" in miemail and contador_guion<2:
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".eu" in miemail and contador_guion<2:
		print("el email es correcto")

elif contador_punto<4 and "@" in miemail and ".com.ar" in miemail and contador_guion<2: #jara.acosta@gmail.com.ar (aquí fallaría, porque hay 3 puntos, por tanto le digo a contador<4)
		print("el email es correcto")

elif cuenta_arroba>1:
	print("email incorrecto")


else:
	print("email incorrecto")