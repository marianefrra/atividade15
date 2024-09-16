# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

n1 = float(input("digite o primiro número"))
n2 = float(input("digite o segundo número"))

operacao = input("digite a operaçã que deseja utilizar; soma, subtração, multiplicação ou divisão")

if operacao == "soma":
    print(n1 + n2)
elif operacao == "subtração":
    print(n1 - n2)
elif operacao == "multplicação":
    print(n1 * n2)
if operacao == "divisão":
    print(n1 / n2)