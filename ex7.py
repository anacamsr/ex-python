#ler uma palavra e informar quantas letras tem essa palavra

cont = 0
palavra = input('digite a palavra: ')
for letra in palavra:
    if letra != " ":
        cont = cont + 1
        print(cont)