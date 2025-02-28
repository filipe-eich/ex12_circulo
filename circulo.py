"""
Programa: circulo
Descrição: Este programa calcula a circunferência e área de um círculo informado pelo Usurário.
Autor: Filipe Eich
Data: 28/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

a=""
c=""
r=""


#Entrada de dados

r = float(input("\nOlá! Vamos calcular a circunferência de área de um círculo? Comece me dizendo o valor do raio: "))


# Processamento de dados

a=3.14159265359*r
c=2*3.14159265359*r


#Saida de dados

print(f"\nA circunferência do círculo mede {c} e a área mede {a}")
