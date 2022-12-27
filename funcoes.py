from typing import List, Tuple
from atomos import Atomos


CONST_AVOGRADO: float = 6.022 * (10**23)


def verificar_elementos(sigla: str="H") -> Tuple[str, str]:
    """Verifica se a Sigla fornecida pertence a Tabela Periódica."""
    siglas: List[str] = [ elemento['sigla'] for elemento in Atomos.propriedades ]
    
    return ( "Elemento não encontrado, tente novamente.", ""
        ) if sigla not in siglas else (
        Atomos.propriedades[siglas.index(sigla)]['massa atômica'],
        Atomos.propriedades[siglas.index(sigla)]['nome'])
    

def calc_massa_molar(massa_atomica: float, nome: str) -> str:
    """Realiza os cálculos se houver o elemento fornecido"""
    if nome: 
        massa_molar: float = massa_atomica / CONST_AVOGRADO
        return f"A massa molar do {nome} é \n{massa_molar:.3e} g/mol"
    else:
        return f"Só é possivel calcular a massa \nmolar para elementos conhecidos."

 
def calcular_massa_molar_de_elemento(sigla: str="H"):
    return calc_massa_molar(*verificar_elementos(sigla=sigla))




if __name__ == "__main__":
    resultado = calcular_massa_molar_de_elemento('Cu')
    print(resultado)
    