#Crie um programa que receba uma notas de avaliações em uma quantidade definida pelo usuário, calcula a média e exibe o resultado. Ao terminar envie para o repositório do GitHub e poste o link.
numeros = [] # guarda as notas digitadas
quantidadeNotas = int(input('Informe a quantidade de notas que deseja inserir: '))

while quantidadeNotas >= 1:

    notas = int(input('Informe uma nota: ')) # notas recebe os numeros digitados
    numeros.append(notas)
    quantidadeNotas -=1 # -=1 diminui 1 do contador
print(numeros)
    
media = sum(numeros)/ len(numeros)
print(media)