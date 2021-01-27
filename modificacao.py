import pandas as pd

dic_alunos = {'M01':'Seinfeld', 'M02':'George', 'M03':'Kramer', 'M04':'Elaine'}
alunos = pd.Series(dic_alunos)


print('# para inserir')
alunos['M05'] = 'Newman'
print(alunos)

print('# alterar')
alunos['M03'] = 'Cosmo'
print(alunos)

print('# remover')
alunos = alunos.drop('M05')
print(alunos)