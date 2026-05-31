from datetime import datetime
from classes.ControleFinanceiro import ControleFinanceiro

class Receita(ControleFinanceiro):
    def __init__(self, valor_bruto: float, setor: str):
        self.setor = setor
        self.valor_bruto = valor_bruto
        self.data = self.obter_data()

        self.imposto1 = 0.08 # valor_bruto total <= 6000
        self.imposto2 = 0.24 # valor_bruto total <= 15000
        self.imposto3 = 0.33 # valor_bruto total > 30000

    def calcular_imposto(self) -> float:
        if 0 < self.valor_bruto <= 6000:
            return self.valor_bruto * self.imposto1
        elif 6000 < self.valor_bruto <= 15000:
            return self.valor_bruto * self.imposto2
        else:
            return self.valor_bruto * self.imposto3
    
    def calcular_liquido(self) -> float:
        return self.valor_bruto - self.calcular_imposto()

    def obter_data(self) -> str:
        return datetime.now().strftime('%d/%m/%Y às %H:%M')