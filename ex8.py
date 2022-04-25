# programa que leia dois numeros inteiros e gere o intervalo entre os dois números,
# garantindo que o 1º númeroseja menor que o segundo (não funciona)

num1 = int(input('1º número: '))
num2 = int(input('2º número: '))

if(num1 >= num2):
    print('Segundo número não é maior')
else:
    for i in range (num1, num2):
        print(i)