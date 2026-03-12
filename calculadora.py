valor = float(input("valor do item: "))
quantidade = int(input("quantidade: "))
total = valor * quantidade
desconto = total * 0.1
total_final = total - desconto
print("total com desconto: R$", total_final)
