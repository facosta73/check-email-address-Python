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


if 1<contador_punto<3 and "@" in miemail and ".com" in miemail:   #aquí está FALLANDO con mateo@gmail.com
		print("el email es correcto")

elif 1<contador_punto<3 and "@" in miemail and ".es" in miemail:
		print("el email es correcto")

elif 1<contador_punto<3 and "@" in miemail and ".org" in miemail:
		print("el email es correcto")

elif 1<contador_punto<3 and "@" in miemail and ".eu" in miemail:
		print("el email es correcto")

elif 1<contador_punto<4 and "@" in miemail and ".com.ar" in miemail: #jara.acosta@gmail.com.ar (aquí fallaría, porque hay 3 puntos, por tanto le digo a contador<4)
		print("el email es correcto")									#ERROR:  me dá correcto: jara-acosta@gmail.com.ar           Y esto porqué???????
																		# creo que es porque toma el guión como una letra más.

																		# me dá incorrecto con: jara-acosta@gmail.com, (porque tiene un solo punto).
																		# y TAMBIEN para lo más simple: mateo@gmail.com (porque tiene un solo punto)
																		# y jara@@gmail.com , da error por un solo punto, que deja pasar hasta llegar al elif del cuenta_arroba: incorrecto

elif cuenta_arroba>1:
	print("email incorrecto")

else:
	print("email incorrecto")