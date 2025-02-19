carne = input("Qual carne deseja [F]ilé duplo, [A]lcatra ou [P]icanha: ").upper()
peso = float(input("Digite quantos quilos dessa carne vai comprar: "))
pagamento = input("Formas de pagamento: [D]inheiro ou [C]artão tabajara (5% de desconto)? ").upper()
preco_total = 0

print("****Hipermercado Tabajara****\nCupom fiscal\n")

if carne == "F":
    print("Item: Filé Duplo")
    if peso > 5:
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9

elif carne == "A":
    print("Item: Alcatra")
    if peso > 5:
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9

elif carne == "P":
    print("Item: Picanha")
    if peso > 5:
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9

print(f"Quantidade: {peso:.2f}Kg")
print(f"Preço total: R${preco_total:.2f}")

if pagamento == "D":
    print("Pagamento em: Dinheiro")
    desconto = 0
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")

elif pagamento == "C":
    print("Pagamento em: Cartão Tabajara")
    desconto = preco_total * 5 / 100
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")