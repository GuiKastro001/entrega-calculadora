op = input('Digite a operação desejada(Soma/Sub/Div/Mult):')

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))

#Soma
if op == 'Soma':
    res = num1 + num2
    print(f'O resultado desta soma é: {res}')

#Subtração
elif op == 'Sub':
    res = num1 - num2
    print(f'O resultado desta subtração é:{res}')

#Divisão
elif op == 'Div':
    res = num1 / num2
    print(f'O resultado desta divisão é:{res}')

#Multiplicação
elif op == 'Mult':
    res = num1 * num2
    print(f'O resultado desta multiplicação é:{res}')

# Owo