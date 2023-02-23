oper = input('Digite a operação desejada(Soma/Sub/Div/Mult):')

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))

if oper == 'soma' or 'Soma':
    res = num1 + num2
    print(f'O resultado desta soma é: {res}')
elif oper == 'Sub' or 'sub':
    res = num1 - num2
    print(f'O resultado desta subtração é:{res}')
elif oper == 'div' or 'Div':
    res = num1 / num2
    print(f'O resultado desta divisão é:{res}')
elif oper == 'Mult' or 'mult':
    res = num1 * num2
    print(f'O resultado desta multiplicação é:{res}')