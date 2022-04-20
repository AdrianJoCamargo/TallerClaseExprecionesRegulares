import re
print("Escriba una contraseña con el siguiente orden: ")
print('Tres letras mayusculas, tres digitos, tres letras minusculas, tres caracteres especiales y un @')
contra=input()
limit=re.compile(r'([A-Z]{3})([0-9]{4})([a-z]{3})([^a-z|A-Z|0-9|@]{3})(@)')
if limit.search(contra):
    print("Contraseña cumple con todos los requisitos")
else:
    print("La contraseña no cumple todos los requisitos")
