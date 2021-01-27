import pandas as pd
notas = pd.Series([7.5, 8.0, 9.5, 6.0])
dic_alunos = {'M01':'Seinfeld', 'M02':'George', 'M03':'Kramer', 'M04':'Elaine'}
alunos = pd.Series(dic_alunos)

## Para verificar se existe um indice com determinado valor, basta usar o operador IN do python, retorna um booleano
existe_m01 = 'M01' in alunos
print(existe_m01)

## Para verificar se há um dado, se utiliza o método isin() do pandas
existe_George = alunos.isin(['George'])
print(existe_George)