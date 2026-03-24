def realizar_login():

    print ('\nTela de login - Meet\n')

    nome_usuario = input('Digite seu login para continuar :')

    senha_usuario = input ('Digite sua senha para continuar: ')

    print = (f'Bem-vindo, {nome_usuario}! ')

    print ('------------------------------\n')

    realizar_login()

import getpass

def realizar_login_invisivel():
    
    senha_padrao= "1234"
    print('\n--- Sistema de Login Seguro ---')
    nome_usuario = input ('Digite seu login')
    senha_usuario = input ('Digite sua senha')

    senha_digitada = getpass.getpass('Digite sua senha (os caracteres não aparecerão): ')

    if senha_digitada == senha_padrao:
       print (f'\n[SUCESSO] Bem-vindo, {nome_usuario}! ')
    else:
        print('\n[ERRO] Senha Incorreta! ')
        
    print ('-----------------------------\n')

realizar_login_invisivel()