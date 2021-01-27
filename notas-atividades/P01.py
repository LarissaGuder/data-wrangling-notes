import pandas as pd

#Cria a Series notas sem especificar index
notas = pd.Series([7.5, 8.0, 9.5, 6.0])
print("Notas >>>");
print(notas);
print("-----------");

#Cria a Series alunos especificando index
lst_matriculas = ['M01','M02','M03','M04']
lst_nomes = ['Seinfeld','George','Kramer','Elaine']
alunos = pd.Series(lst_nomes, index=lst_matriculas)
print("Alunos >>>");
print(alunos);
print("----------- >>");

#Cria a Series usando dict
dic_alunos = {'M01':'Seinfeld', 'M02':'George', 'M03':'Kramer', 'M04':'Elaine'}
alunos = pd.Series(dic_alunos)
print("Alunos usando dicionário >>>");
print(alunos);
print("----------- >>");

## Tipos de elementos do Pandas
## dtype | Utilização | Tipo Python
## int64 | num inteiros | int
## float64 | num reais | float
## bool | True/False | bool
## object | texto | String
## datetime64 | data/hora | datetime

## dtype não é a mesma coisa que tipo do objeto (type)

### Demais propriedades elementares
## values: vetor de dados
## index: vetor de rótulos
## name: nome do vetor de dados
## size: tamanho da Series (número de elementos)
## index.name: nome do vetor de rótulos
## index.dtype: dtype do vetor de rótulos