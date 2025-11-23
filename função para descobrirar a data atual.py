from datetime import datetime
from time import sleep



def retornar_data_atual():
    """
    A função retornará a data de quando o programa foi rodado
    """
    momento_atual = datetime.now()
    
    
    data_formatada = momento_atual.strftime("Data: %d/%m/%y \nHora da anotação: %H:%M:%S") # "%d" = data "%m" = mês "%y" = Ano
    
    return data_formatada


data_atual = retornar_data_atual()
    

