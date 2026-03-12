nome = input('digite o seu nome: ')
quantidade_produtos = int(input('digite a quantidade de produtos vendidos: '))
valor_produtos = float(input('digite o valor do produto: '))

print(f'o valor final foi de: {valor_produtos * quantidade_produtos}')

valor_final = valor_produtos * quantidade_produtos

if valor_final >= 4000.0:
    print('parabens voce teve um superavit')
else:
    print('poxa voce teve um defit')



