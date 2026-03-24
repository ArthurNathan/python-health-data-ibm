# Anonimizador de nomes de pacientes
nome = "Matheus Souza Lemes"
lista_nome = nome.split()
resultado = ""
for i in lista_nome:
    resultado = resultado + (i[0]+".").upper()
print(resultado)
