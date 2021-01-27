import pandas as pd
notas = pd.Series([7.5, 8.0, 9.5, 6.0])
dic_alunos = {'M01':'Seinfeld', 'M02':'George', 'M03':'Kramer', 'M04':'Elaine'}
alunos = pd.Series(dic_alunos)

## Tradicional
print(alunos[0])
print(alunos['M01'])

## Ao usar valores negativos, é pego na ordem inversa (último elemento)
print(alunos[-1])
# ou
print(alunos[alunos.size-1])

## Usando slicing
# Sintaxe | Explicação
# s[i:j] | do elemento do indice i ao indice j-1
# s[i:] | do elemento i até o último
# s[:j] | do primeiro elemento até o elemento do indice j-1
# s[-k:] | últimos k elementos
# s[i:j:k] | do elemento i até o elemento j (pulando) passo k elementos
# s[[lista]] | todos elementos especificados na lista

print(alunos[0:3])

## Booleana
# seleção com base nos valores de dados
idx_aprovados = notas[notas >= 7].index
print("Aprovados >> ")
print(alunos[idx_aprovados])