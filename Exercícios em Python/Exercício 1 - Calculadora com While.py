'''Calculadora com while'''

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador [+ - / *]: ')

    numeros_validos = None


    #converter numero para float e validar para uso
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos numeros nao estao validos')
        continue


    #Checar se o operador esta valido
    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Não pode mais que um operador')
        continue

    
    #Fazendo a conta
    print('Resultado Abaixo: ')
    if operador == '+':
        print( num_1_float + num_2_float )
    elif operador == '-':
        print( num_1_float - num_2_float )
    elif operador == '*':
        print( num_1_float * num_2_float )
    elif operador == '/':
        print( num_1_float / num_2_float )


    #Saida do codigo
    sair = input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True:
        break


