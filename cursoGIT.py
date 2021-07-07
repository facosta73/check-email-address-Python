# Primeros ejercicios en Python: check email address. primeras versiones



# Primero hago un INPUT para que pida un email, luego hago dos BUCLES con CONTADORES para chequear cada caracter del email y contabilice arrobas y puntos.
#Y luego CONDICIONALES para que cumpla o prohiba diferentes situaciones

#corrijo el doble @

#con el tipo jara.acosta@gmail.com.ar (aquí fallaría, porque hay 3 puntos, por tanto le digo a contador_punto<4)

#corrijo el doble punto ".."

# direcciones email a probar:
# jara@gmail.com
# jara.acosta@gmail.com
# jara.gmail.com
# jara@acosta@gmail.com (aquí en el anterior código mas aceptable, me contaba 3 caracteres y lo daba por bueno)
# jara.acosta@gmailcom (in punto antes del com)
# jara..acosta@gmail.com
# jara.acosta@gmail..com
# jara@acosta@gmail.com
# jara.acosta@@gmail.com
# jara_acosta@gmail.com
# jara__acosta@gmail.com
# jara-acosta@gmail.com
# jara--acosta@gmail.com
# jara acosta@gmail.com


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
	print("email incorrecto, no puede usar dos @")

elif ".." in miemail:
	print("email incorrecto, no use doble punto")

elif " " in miemail:
	print("email incorrecto, no use espacios")	

elif "__" in miemail:
	print("email incorrecto, no use doble guion")

elif "--" in miemail:
	print("email incorrecto, no use doble guion")

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
