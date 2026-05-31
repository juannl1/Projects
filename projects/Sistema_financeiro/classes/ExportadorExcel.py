from classes.Exportador import Exportador
import pandas as pd

class ExportadorExcel(Exportador):
    def exportar(self, dados: list, nome_arquivo: str = "relatorio_financeiro.xlsx"):
        df = pd.DataFrame(dados)

        with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Planilha Financeira', index=False)
            worksheet = writer.sheets['Planilha Financeira']

            for col in worksheet.columns:
                max_len = max(len(str(cell.value or '')) for cell in col)
                col_letter = col[0].column_letter
                worksheet.column_dimensions[col_letter].width = max(max_len + 3, 12)
                
        print(f"Planilha Excel gerada: {nome_arquivo}")