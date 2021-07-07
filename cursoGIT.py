#check email address. primeras versiones

#ejercicio para emails, por ahora el mejor al 21/06/21. Falla para facosta73@gmail..com


miemail=input("Introduzca su dirección de email: ")

cuenta_arroba=0
for a in miemail:
	if(a=="@"):
		cuenta_arroba=cuenta_arroba+1


contador_punto=0
for i in miemail:
	if(i=="."):
		contador_punto=contador_punto+1

contador_doblepunto=0
for d in miemail:
	if(d==".."):
		contador_doblepunto=contador_doblepunto+1



if cuenta_arroba>1:
	print("email incorrecto")

elif contador_doblepunto>0:
	print("email incorrecto")

elif contador_punto<3 and "@" in miemail and ".com" in miemail:   #podría probar poniendo un elif tipo elif "..com" in miemail print "incorrecto"
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