# Anonimizador de nomes de pacientes
nome = "Arthur-Nathan Luiz"
lista_nome = nome.split()
resultado = ""
for i in lista_nome:
    resultado = resultado + (i[0]+".").upper()
print(resultado)
