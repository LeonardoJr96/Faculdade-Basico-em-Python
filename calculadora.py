resultado = 0
repetir = 'sim'

while repetir == 'sim':

    numero_1 = float(input("digite um número: "))
    sinal = str(input("digite o sinal: "))
    numero_2 = float(input("digite outro número: "))

#somar
    if sinal == '+':
        resultado = numero_1 + numero_2
    else:
#subtrair
        if sinal == '-':
            resultado = numero_1 - numero_2
#multiplicar
        if sinal == '*' or sinal == 'x':
            resultado = numero_1 * numero_2
#dividir
        if sinal == '/':
            resultado = numero_1 / numero_2
#potência
        if sinal == '**':
            resultado = numero_1 ** numero_2

    print(resultado)
    repetir = str(input('quer fazer um novo calculo? '))

else:
    print('fim')
