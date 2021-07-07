#check email address. primeras versiones

#ahora corrijo el fallo para el correo mas simple, donde hay solo un punto, por tanto le saco el 1< al contador_punto: jara@gmail.com
#pero da correcto para jara@@gmail.com, voy a probar subir el elif de cuenta_arroba al ppio del bloque de condicionales

miemail=input("Introduzca su dirección de email: ")

cuenta_arroba=0
for a in miemail:
	if(a=="@"):
		cuenta_arroba=cuenta_arroba+1


contador_punto=0
for i in miemail:
	if(i=="."):
		contador_punto=contador_punto+1


if contador_punto<3 and "@" in miemail and ".com" in miemail:   
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".es" in miemail:
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".org" in miemail:
		print("el email es correcto")

elif contador_punto<3 and "@" in miemail and ".eu" in miemail:
		print("el email es correcto")

elif contador_punto<4 and "@" in miemail and ".com.ar" in miemail: #jara.acosta@gmail.com.ar (aquí fallaría, porque hay 3 puntos, por tanto le digo a contador<4)
		print("el email es correcto")

elif cuenta_arroba>1:
	print("email incorrecto")

else:
	print("email incorrecto")