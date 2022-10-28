cima_h = 1
baixo_h = 1
cima_s = 1
baixo_s = cima_s * cima_s
cima_p = 2
base_p = 1
divisor = None
h = cima_h/baixo_h
s = cima_s/baixo_s
p = cima_p/(base_p ** 3)
count_h = 1
count_s = 1
count_p = 1
n = int(input('Informe N: '))


while n < 50:
    print('N deve ser igual ou maior a 50...')
    n = int(input('Informe N: '))


while cima_h < (n*2 - 1) and baixo_h < n:
    cima_h += 2
    baixo_h += 1
    count_h += 1
    if count_h % 2 == 0:            # se o contador for par, o número é positivo
        h += cima_h/baixo_h
    else:                           # se o contador for ímpar, o número é negativo
        h -= cima_h/baixo_h


while cima_s < n and baixo_s < (n*n):
    cima_s += 1
    baixo_s = cima_s * cima_s
    count_s += 1
    if count_s % 2 == 0:            # se o contador for par, o número é negativo
        s -= cima_s/baixo_s
    else:                           # se o contador for ímpar, o número é positivo
        s += cima_s/baixo_s


while count_p < n:
    while True:
        cima_p += 1
        for c in range(1, cima_p):
            if cima_p % c == 0:     # para achar os divisores de cima_p
                divisor = c
        
        if divisor == 1:            # achou o numero primo
            break
    
    base_p += 2
    p += cima_p/(base_p ** 3)
    count_p += 1




print(f'H = {h:.4f}')
print(f'S = {s:.4f}')
print(f'P = {p:.4f}')
