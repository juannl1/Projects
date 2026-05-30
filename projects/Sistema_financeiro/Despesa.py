from datetime import datetime
from ControleFinanceiro import ControleFinanceiro


class Despesa(ControleFinanceiro):
    def __init__(self, valor_saida:float, setor:str):
        self.valor_saida = valor_saida
        self.setor = setor
        self.data = self.obter_data()

    def calcular_imposto(self) -> float:
        return 0.0

    def calcular_liquido(self) -> float:
        return (self.valor_saida * 2) - (self.valor_saida * 4)

    def obter_data(self) -> str:
        return datetime.now().strftime('%d/%m/%Y às %H:%M')

    def calcular_lucro(self, liquido):
        return liquido + self.valor_saida

def testando():
    despesa = Despesa(1000, "TI")

    print(despesa.calcular_imposto())
    print(despesa.calcular_liquido())
    print(despesa.obter_data())

#testando()