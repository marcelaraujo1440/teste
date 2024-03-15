print('Escolha uma operação:')
print('1-Adiçao')
print('2-Subtração')
print('3-Multiplicação')
print('4-Divisão')
print('5-Sair')

escolha=input('Escolha uma operação: ')
if escolha=='5':
    print('Saindo da Calculadora...')
    continuar=False
elif escolha in ['1','2','3','4']:
    n1=float(input('Digite o primeiro número: '))
    n2 =float(input('Digite o segundo número: '))

if escolha=='1':
    resultado=(n1+n2)
    print(f'o resultado da soma é de {resultado} ')
elif escolha=='2':
    resultado=(n1-n2)
    print(f'O resultado da divisão foi de {resultado}')
elif escolha=='3':
    resultado=(n1*n2)
    print(f'O resultado da multiplicação foi de {resultado}')
elif escolha=='4':
        resultado=(n1/n2)   
        print(f'O resultado da divisão foi de {resultado}')
elif escolha=='5':
    print('Tente com outra operação, você está fora da calculadora!')
else:
    print('Não foi possível encontrar o que você deseja!')

