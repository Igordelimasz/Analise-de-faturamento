email = input(' digite o seu email: ')
senha = input(' digite a sua senha: ')
print('cadastro realizado com sucesso')

email_login = input('digite o seu email: ')
senha_login = input('digite sua senha: ')

if email_login == email and senha_login == senha:
    print('login realizado com sucesso')
else:
    print('email ou senha incorreto')

