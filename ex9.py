#programa  que leia 10 números e imprima a quantidade de números pares e ímpares exixtentes entre eles.

cont_par = 0
cont_imp = 0
for i in range(1,11):
     num = int(input())
     if(num %2 ==0):
         cont_par = cont_par+1
else:
    cont_imp = cont_imp+1
    print('quantidade de pares: ', cont_par)
    print('quantidade de impares: ', cont_imp)
