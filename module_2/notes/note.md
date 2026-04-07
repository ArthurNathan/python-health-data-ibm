# Module 2
## Resume
Utilizando os conceitos de estrutura de dados, eu pude perceber como informações
podem ter propriedades básicas: serem int, float, str, boolean. Por sua vez, estes tipos básicos de "informação" podem 
ser agrupados em objetos como, tuplas, listas, dicionários e conjuntos.Cada um destes 4 outros objetos, tem propriedades
específicas, nos permitindo manipular e/ou receber/enviar informações de maneiras diferentes.
A tuplas, representadas por X = ( ,  , ,) são objetos ordenados, que contém outros objetos; são imutáveis.
O que significa que  podemos manipular X, acessar seu "conteúdo" através de uma indexação,mas não é possível  alterar o
conteúdo; ( , , , ), continuará igual, porém podemos gerar outros objetos a partir da tupla original.
Listas X = [ ,  ,  , ] são objetos ordenados e mutáveis.
Dicionários  são objetos  não ordenados*. Cada elemento do dicionário é um par "chave-valor", X = {"chave": valor, "": , }.
Para acessar o conteúdo, é necessário acessar mediante a chave, não através de um indíce. 
Já os Conjuntos(set), pelo que entendi, são iguais aos conjuntos da teoria de conjuntos matemática. Mutáveis, não ordenados
e operáveis tal qual a teoria axiomática de conjuntos. X = { , , , }.

Este é um breve resumo do que estou relembrando do meio de semana.

## Reflecções
Uma consequência das definições acima, e conectando com a minha pequena experiência em bioestatística é que se eu for pensar 
numa tabela, tal qual aquelas analisadas nos projetos de tcc, pic, etc, A unidade amostral sempre era representada por uma,
linha. 
Na linha 1, tinha o paciente x, com, por exemplo, peso, idade, sexo, local... Para que eu conseguisse rodar os testes estatis
ticos de interesse, a minha planilha do excell tinha de estar desta forma. Ao que me parece, existem algumas maneiras de
estruturar dados, de modo a ter algo parecido:
*Listas simples*
- Paciente01 = [18anos, Masculino, 140/90 Mmhg, ..., ] 
- Paciente02 = [ Idade, Sexo, Pa, ..]

*Dicionários com listas*
Pacientes = {"Paciente01": [18anos, Masculino, 140/90 Mmhg, ..., ], "Paciente02":  [Idades,Sexo, Pa, ..., ], ..} 

*Listas com dicionários*
Pacientes = [{"Paciente01": [18anos, Masculino, 140/90 Mmhg, ...,]},{"Paciente02": [Idades,Sexo, Pa, ..., ]},...]
Essa acima recolve uma coisa, é o fato de agora termos possibilidade de indexar o par "chave-valor".

*Listas com listas*
Pensei um pouco mais sobre o problema da indexação acima e acredito que o melhor jeito seja trabalhar com listas mesmo; eu 
posso, fazer indíce de índice. Olhando para o Excell eu tinha acesso a toda informação disponível, eu sabia qual eram as ini
ciais do paciente, sexo, eu consegui localizar cada característica da minha unidade amostral, acessando dizendo em qual linha
e qual coluna. Com a maneira acima, lista com dicionários, eu não resolvo isso. Porém, se eu estruturar assim:

-pacientes = [["paciente01",1,2,3,4,5], ["paciente02",1,2,8,2,7]]

Da maneira acima, basta fazer pacientes[0][0], para acessar, "paciente01", por exemplo.

Tentei linkar o que estou aprendendo com minha experiência durante a faculdade, imagino que no decorrer do aprendizado
saberei qual das soluções é a ideal, para determinados contextos.




* Aparentemente, desde a versão 3.6, dicionários tem sua ordem de inclusão de item preservado, sempre vou ter na tela, um
print, por exemplo, da sequência original do dicionário. Porém, ao  comparar dois dicionários que tem ordem de inclusão dife-
rentes, mas os mesmos itens, '==', o resultado é True. Pelo jeito, a ordem tem um relevância, mas não tanto quanto na tupla
ou lista. Atualização: Ao iterar, a ordem segue a ordem de inserção.

** Após discutir com o GPT, me ele me explicou qual seria a melhor forma de transformar uma tabela, seria utilizando uma lista de dicionários:

pacientes = [{"nome": "João", "idade": 65}, {"nome": "Maria", "idade": 45}]

Deste jeito há legibilidade, além disso, é possível acessar toda informação, utlizando os valores da chaves e o índex inicial. Por exemplo, pacientes[0]["idade"] me retornaria 65, se fosse apenas pacientes[0], eu teria a linha com as características do paciente em questão; assim, número da linha, seria o paciente e os nomes das chaves, as colunas
