import webbrowser
from atomos import Atomos
from funcoes import verificar_elementos




def _abre_browser(url: str) -> None:
    webbrowser.open(url)

def abre_equacao(resultado, sigla):
    nome = verificar_elementos(sigla.lower())

    print('nome',nome)
    resultado = resultado.replace(' g/mol','')
    resultado = resultado.split('e')
    num, exp = resultado[0], resultado[1]
    equacao = rf"https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B300%7D%20%5Chuge%20{sigla}_%7Bmm%7D%20%20%3D%20%7B{num}%7D.10%5E%7B{exp}%7Dg/mol%5C%5C*{sigla}%20%5Cto%20{nome[1]}%5C%5C*mm%20%5Cto%20massa%5C%20molar"
    _abre_browser(equacao)
    