from socket import *
import pandas as pd
dados = pd.read_json('dados.json')

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)

#atribui a porta ao  socket  criado
serverSocket.bind(('', serverPort))
#aceita  conexoes com no  maximo  um  cliente  na fila
serverSocket.listen(1)
print('The  server  is  ready to  receive ')
while True:
    connectionSocket, addr = serverSocket.accept()
    #recebe a mensagem  do  cliente  em  bytes
    mensagem = connectionSocket.recv(1024)
    #envio  tbm  deve  ser em  bytes
    mensagem = mensagem.decode()
    x = mensagem.split()
    mat = x[0]
    dis = x[1]
    nota = x[2]

    c = dados[dados['matricula'] == int(mat)]
    disciplinas = c['disciplina'].apply(pd.Series)
    d = disciplinas[dis]
    n = d.apply(pd.Series)
    mensagem = str(int(n[nota]))

    connectionSocket.send(mensagem.encode())
    connectionSocket.close()
