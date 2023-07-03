print()

"""
    Argumentos nomeados e não nomeados em funções python
    Argumentos nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor)

"""
import os
import math

a = input("Digite um numero para A:")
b = input("Digite um numero para B:")
c = input("Digite um numero para C:")

ax = float(a)
bx = float(b)
cx = float(c)

def calcular_baskara(a, b, c):
    discriminante = b**2 - 4*a*c
    print("\nDelta = ", discriminante)
    
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return "Impossivel calcular."
    
    

# Exemplo de uso da função
# raizes = calcular_baskara(-7, 3, 5)
# calcular_baskara(ax, bx, cx)
""" raizes = calcular_baskara(ax, bx, cx)
print(raizes) """

# def  soma(x, y):
#     print(x + y)

# soma(10, 5)

# def  mult(x, y):
#     print(x * y)

# mult(10, 5)

# def  subtrair(x, y):
#     print(x - y)

# subtrair(10, 5)

# v1 = input("Digite os valores para A, B e C:\n").split()
v1 = input("Digite os valores para A:")
v2 = input("Digite os valores para B:")
v3 = input("Digite os valores para C:")

os.system("cls") # Limpa o terminal
print("Primeira formula")
raizes = calcular_baskara(ax, bx, cx)
print(raizes)

print()
# a, b, c = v

a = float(v1)
b = float(v2)
c = float(v3)
""" a = float(a)
b = float(b)
c = float(c) """
print("Segunda formula")
print()

if a == 0.0  or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))