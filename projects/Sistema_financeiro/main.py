from GerenciadorFinanceiro import GerenciadorFinanceiro
from Receita import Receita
from Despesa import Despesa
from ExportadorExcel import ExportadorExcel
from ExportadorJSON import ExportadorJSON


def executar_sistema():
    gerenciador = GerenciadorFinanceiro()

    receita_TI = Receita(106352.54, "Desenvolvimento de Software")
    receita_Marketing = Receita(11249.32, "Marketing")

    despesa_Financeiro = Despesa(4000, "Financeiro")
    despesa_devs = Despesa(30000, "Equipe de desenvolvimento")
    despesa_marketing = Despesa(1621, "Marketing")

    gerenciador.adicionar_receita(receita_TI)
    gerenciador.adicionar_receita(receita_Marketing)

    gerenciador.adicionar_despesa(despesa_devs)
    gerenciador.adicionar_despesa(despesa_Financeiro)
    gerenciador.adicionar_despesa(despesa_marketing)

    gerar_planilha = ExportadorExcel()
    gerar_JSON = ExportadorJSON()
    gerar_planilha.exportar(gerenciador.dados_relatorio())
    gerar_JSON.exportar(gerenciador.dados_relatorio())


executar_sistema()