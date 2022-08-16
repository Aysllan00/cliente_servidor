import pandas as pd
dados = pd.read_json('dados.json')
'''
mat = 1453
dis = '03'
nota = 'n2'
'''
mat0 = input('Matricula: ')
dis0 = input('Disciplina: ')
nota0 = input('Nota: ')

mens = mat0 + ' ' + dis0 + ' ' + nota0

x = mens.split()
mat = x[0]
dis = x[1]
nota = x[2]

c = dados[dados['matricula'] == int(mat)]
disciplinas = c['disciplina'].apply(pd.Series)
d = disciplinas[dis]
n = d.apply(pd.Series)
msg = str(int(n[nota]))
print(msg)
