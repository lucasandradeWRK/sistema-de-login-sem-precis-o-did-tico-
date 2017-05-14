print('''--------Criar_conta---------------

''')
usuario = input('username--> ')
senha = input('informe sua senha--> ')
def criador(usuario, senha):
    import pickle
    usuarios = {}
    usuarios[usuario]=senha
    dados = open('Dados.txt', 'wb')
    pickle.dump(usuarios, dados)
    dados.close()
criador(usuario, senha)
import login
