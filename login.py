import pickle
dados=open('Dados.txt', 'rb')
usuarios = pickle.load(dados)
dados.close()

print('---------------acessar a conta---------------')

usuario = input('username--> ')
if usuario not in usuarios:
  while usuario not in usuarios:
        usuario = input('usuario inexistente, informe novamente--> ')
senha = input('senha--> ')
if usuarios[usuario]==senha: #o conteudo do dicionário é a senha, ai ele vai 
#se a senha (conteúdo do dicionario) é igual a senha informada pelo usuário
  print('bem vindo', usuario)
else:
  while senha not in usuarios[usuario]:
        senha = input('senha incorreta, tente novamente--> ')
  print('Bem vindo', usuario)#obs: tanto faz o escope desta, fora ou dentro do
  #else ja que este print só sera exibido no final do programa, e o final do
  #programa, só chega quando o usuario consegue logar(entrar)
