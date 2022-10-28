from random import randint


#NUMEROS = 10        

ultimo_numero = None

soma_a = 0
contador_a = 1
maior_soma_a = 0
maior_sequencia_a = 0

maior_b = None
contador_b = 1
maior_soma_b = 0
maior_sequencia_b = 0

# for n in range(NUMEROS):                    
#     entrada = int(input("Numero: "))        
for n in range(0, 150):
    entrada = randint(0, 10)
    print(entrada)

    if ultimo_numero and ultimo_numero == entrada - 1:
        print('Contabilizou a')             
        soma_a += entrada
        contador_a += 1
        contador_b = 1

        if (contador_a == maior_sequencia_a and soma_a > maior_soma_a) or contador_a > maior_sequencia_a:
            maior_soma_a = soma_a
            maior_sequencia_a = contador_a

    elif ultimo_numero and ultimo_numero == entrada:
        print('Contabilizou b')
        contador_a = 1
        soma_a = entrada
        contador_b += 1

        if contador_b > maior_sequencia_b or (contador_b == maior_sequencia_b and entrada > maior_b):
            maior_b = entrada
            maior_sequencia_b = contador_b


    else:
        contador_a = 1
        soma_a = entrada
        contador_b = 1
        print('Não contabilizou')
        

    ultimo_numero = entrada


if maior_sequencia_a != 0:
    print(f"Maior sequencia em ordem crescente: {maior_sequencia_a}\nsoma = {maior_soma_a}")
else:
    print('Não houve sequência consecutiva de números em ordem crescente!')

if maior_b and maior_sequencia_b != 0:
    print(f"Maior sequencia de números constantes: {maior_sequencia_b}\nNúmero = {maior_b}")
else:
    print('Não houve sequência consecutiva de números constantes!')

