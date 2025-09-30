print("Calculando descontos\n\n")

valor_da_compra = float(input("Digite o valor da sua compra: "))

"""

entre 50 a 100 reais. desconto de 5%
entre 100 a 500. desconto de 20%
entre 500 +. desconto de 50%

"""

desconto_5_porcento = (valor_da_compra * 0.05)
desconto_20_porcento = (valor_da_compra * 0.20)
desconto_50_porcento = (valor_da_compra * 0.50)

if valor_da_compra >= 50 and valor_da_compra <= 100:
    print(f"Você recebeu 5% de desconto na sua compra...\n\nTotal > > > {valor_da_compra - desconto_5_porcento}")

elif valor_da_compra >= 100 and valor_da_compra <= 500:
    print(f"Você recebeu 20% de desconto na sua compra...\n\nTotal > > > {valor_da_compra - desconto_20_porcento}")

elif valor_da_compra >= 500 and valor_da_compra >= 1000:
    print(f"Você recebeu 50% de desconto na sua compra...\n\nTotal > > > {valor_da_compra - desconto_50_porcento}")

else:
    print(f"Você não recebeu nenhum desconto....\n\nTotal > > > {valor_da_compra}")
