import datetime
def menu_inicial():
    print('Programa de descontos')
    print('Digite o número correspondente ao seu cadastro')
    print('1. Adulto')
    print('2. Aposentado')
    print('3. Estudante')
    print('4. Desconto do dia')

hoje=datetime.datetime.now().date()

if __name__:
    menu_inicial()
    escolha = input('Escolha a operação que deseja realizar: ')
if escolha == '1' and hoje.isoweekday:
    print('Você recebeu 5% de desconto!')
elif escolha == '2' and hoje.isoweekday:
    print('Você recebeu 15% de desconto!')
elif escolha == '3':
    print('Você recebeu 10% de desconto!')
elif escolha == '4' and hoje.isoweekday:
    print('Você recebeu 2% de desconto!')
else:
    print("Informe um número válido!!")