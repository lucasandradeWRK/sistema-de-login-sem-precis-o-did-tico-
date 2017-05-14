print('''
-------------Menu---------------

A)Entrar Na Conta
B)Criar Uma Conta
''')
opçao= input('escolha uma das opções--> ').upper()
if opçao=='A':
    import login
else:
    import criar_conta
   
