pais_a = 15000
pais_b = 45000
pais_c = 65000
taxa_a = 1.10
taxa_b = 1.05
taxa_c = 1.025
anos_para_b = 0
anos_para_c = 0
pais_c_23 = pais_c * 1.23
populacao_a_b = 0
populacao_a_c = 0

while pais_a < pais_b:
    pais_a *= taxa_a
    pais_b *= taxa_b
    anos_para_b += 1
    populacao_a_b = pais_a

pais_a = 15000

while pais_a <= pais_c_23:
    pais_a *= taxa_a
    pais_c *= taxa_c
    pais_c_23 = pais_c * 1.23
    anos_para_c += 1
    populacao_a_c = pais_a


print(f'A população A igualará ou ultrapassará a população B em {anos_para_b} anos,\
já que a população A será de {populacao_a_b:.2f} e a população B será de {pais_b:.2f} ')
print(f'A população A ultrapassará a população C em 23% em {anos_para_c} anos,\
já que a população A será de {populacao_a_c:.2f} e a população C será de {pais_c:.2f} ')
