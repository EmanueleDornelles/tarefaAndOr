nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

if (nota1 + nota2 >= 60) and (nota1 >40) and (nota2>40):
    print('O aluno passou!')
else:
    print('Aluno reprovado.')