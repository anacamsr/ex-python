#Script que tenha 5 números inteiros lidos no teclado, imprima o maior e o menor deles.

maior=9999
menor=9999

for i in range(1,6):
    n=int(input('Leia um número:'))
    if (n < menor):
        menor=n
    if(n > maior):
        maior=n
        print('O maior é: ',maior)
        print('O menor é: ',menor)