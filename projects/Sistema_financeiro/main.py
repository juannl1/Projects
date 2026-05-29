from Despesa import Despesa
from Receita import Receita



receita = Receita(1000, "TI")
print(receita.calcular_imposto())
print(receita.calcular_liquido())
