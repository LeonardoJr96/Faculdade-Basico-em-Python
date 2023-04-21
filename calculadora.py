1# inicial

numero_1 = float(input("digite um número: "))
sinal = str(input("digite o sinal: "))
numero_2 = float(input("digite outro número: "))

2# condições

#somar
if sinal == '+':
    resultado = numero_1 + numero_2
else:
 
#subtrair
    if sinal == '-':
        resultado = numero_1 - numero_2

#multiplicar
    if sinal == '*' and 'x':
        resultado = numero_1 * numero_2

#dividir
    if sinal == '/':
        resultado = numero_1 / numero_2
#potência
    if sinal == '**':
        resultado = numero_1 ** numero_2

3# resultado
(print(resultado))
print('fim')