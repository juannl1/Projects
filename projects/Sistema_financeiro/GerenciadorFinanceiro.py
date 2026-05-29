from Receita import Receita
from Despesa import Despesa


class GerenciadorFinanceiro:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_receita(self, objeto:Receita):
        self.transacoes.append(objeto)

    def adicionar_despesa(self, objeto:Despesa):
        self.transacoes.append(objeto)
    
    def dados_relatorio(self) -> list:
        dados = []

        for objeto in self.transacoes:
            if isinstance(objeto, Despesa):
                despesa = {
                    "data": objeto.data,
                    "tipo": "Despesa",
                    "setor": objeto.setor,
                    "valor_saida": objeto.calcular_liquido()
                }
                dados.append(despesa)

            elif isinstance(objeto, Receita):
                receita = {
                    "data": objeto.data,
                    "tipo": "Receita",
                    "setor": objeto.setor,
                    "valor_bruto": objeto.valor_bruto,
                    "valor_imposto": objeto.calcular_imposto(),
                    "valor_liquido": objeto.calcular_liquido()
                }
                dados.append(receita)
            else:
                print("Deu ruim")
        
        return dados
    

def testando():
    receita1 = Receita(1000, "TI")
    receita2 = Receita(5000, "Marketing")
    receita3 = Receita(10000, "ADM")

    despesa1 = Despesa(1000, "TI")
    despesa2 = Despesa(5000, "Marketing")
    despesa3 = Despesa(10000, "ADM")

    gerenciador = GerenciadorFinanceiro()
    gerenciador.adicionar_despesa(despesa1)
    gerenciador.adicionar_despesa(despesa2)
    gerenciador.adicionar_despesa(despesa3)

    gerenciador.adicionar_receita(receita1)
    gerenciador.adicionar_receita(receita2)
    gerenciador.adicionar_receita(receita3)

    print(gerenciador.dados_relatorio())
    
testando()

