# Lista de pacientes
pacientes = [{"paciente": "João", "idade":32, "altura":170, "hipertensão": False, "diabetes": False},
             {"paciente": "Lourdes", "idade":65, "altura":155, "hipertensão": True, "diabetes": True},
             {"paciente": "Jonas", "idade":33, "altura":185, "hipertensão": False, "diabetes": True},
             {"paciente": "Maria", "idade":29, "altura":145, "hipertensão": False, "diabetes": True}]

#Acesso aos pacientes e características dos mesmos:
print(pacientes[0]["idade"])
print(pacientes[0]["altura"])
print(pacientes[0]["hipertensão"])

# Percorrendo todos os nomes e acesando características
for i in pacientes:
    print(i["paciente"], i["altura"])

# Mostrar só quem tem Hipertensão:
for i in pacientes:
    if i["hipertensão"] == True:
        print(i["paciente"], i["hipertensão"])

# Contagem de Hipertensos:
contagem = 0
for i in pacientes:
    if i["diabetes"] == True:
        contagem = contagem +1
print(contagem)


