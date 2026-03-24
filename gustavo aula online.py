
import getpass

def realizar_login():
 

    print('\nTela de login - Meet\n')

    nome_usuario = input('Digite seu login para continuar: ')
 

    print(f'Bem-vindo,  {nome_usuario}!')

    print('--------------------------\n')

realizar_login()


senha_padrao = "1234"

print('\n--- Sistemade login seguro ---')
nome_usuario = input('digite seu login: ')
senha_digitada = input('digite sua senha: ')

senha_digitada = getpass.getpass('digite sua senha (caracteres nao aparecerao): ')

if senha_digitada == senha_padrao:
    print(f'\n[SUCESSO] Bem-vindo,{nome_usuario}! Acesso concedido. ')
else:
    print('\n[ERRO] Senha incorreta! acesso  negado. ')

print('----------------------------------\n')


realizar_login_seguro()