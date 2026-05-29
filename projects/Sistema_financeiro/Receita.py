from datetime import datetime
from ControleFinanceiro import ControleFinanceiro


class Receita(ControleFinanceiro):
    def __init__(self, valor_bruto: float, setor: str):
        self.setor = setor
        self.valor_bruto = valor_bruto
        self.data = self.obter_data()

        self.imposto1 = 0.08 # valor_bruto total <= 3000
        self.imposto2 = 0.24 # valor_bruto total >= 7500
        self.imposto3 = 0.32 # valor_bruto total >= 10000

    def calcular_imposto(self) -> float:
        if self.valor_bruto > 0 and self.valor_bruto <= 3000:
            return self.valor_bruto * self.imposto1
        
        elif self.valor_bruto > 3000 and self.valor_bruto <= 7500:
            return self.valor_bruto * self.imposto2

        else:
            return self.valor_bruto * self.imposto3
    
    def calcular_liquido(self) -> float:
        return self.valor_bruto - self.calcular_imposto()

    def obter_data(self) -> str:
        return datetime.now().strftime('%d/%m/%Y às %H:%M')
    


def testando():
    receita1 = Receita(3000, "Marketing")
    receita2 = Receita(5000, "Desenvolvimento front-end")
    receita3 = Receita(10000, "Desenvolvimento Back-end")

    print(receita1.calcular_imposto())
    print(receita2.calcular_imposto())
    print(receita3.calcular_imposto())

    print(receita1.calcular_liquido())
    print(receita2.calcular_liquido())
    print(receita3.calcular_liquido())

    print(receita1.data)

#testando()
