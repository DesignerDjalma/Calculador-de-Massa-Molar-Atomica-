import time
from funcoes import calcular_massa_molar_de_elemento
import ttkbootstrap as ttkbs
from constantes import *


class InterfaceTkBS(ttkbs.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=AMBOS, expand=SIM,)

        info_txt = "Forneça um Elemento da Tabela Periódica"
        info = ttkbs.Label(master=self, text=info_txt, width=len(info_txt))
        info.pack(fill=HORIZONTAL, pady=10)

        self.elemento_quimico = ttkbs.StringVar(value="")
        self.criar_form("Sigla", self.elemento_quimico)
        self.criar_caixa_botoes()

        self.resultado_txt = ttkbs.StringVar(value="Resultado: ")
        self.resultado = ttkbs.Label(master=self,textvariable=self.resultado_txt,width=30)
        self.resultado.pack(fill=HORIZONTAL, pady=10)


    def on_calcular(self) -> None:
        """Calcula a massa molar e mostra o resutado na interface."""
        res = calcular_massa_molar_de_elemento(self.elemento_quimico.get())
        print(res)
        self.resultado_txt.set(f"Resultado: {res}")


    def on_cancelar(self) -> None:
        """Limpa os resultados."""
        print("Limpando Resutaldo.")
        self.resultado_txt.set(f"Resultado: ")


    def criar_caixa_botoes(self) -> None:
        container = ttkbs.Frame(self)
        container.pack(
            fill=HORIZONTAL,
            expand=SIM,
            pady=(15, 10))

        btn_cancelar_txt = "Cancelar"
        btn_cancelar = ttkbs.Button(
            master=container,
            text=btn_cancelar_txt,
            width=len(btn_cancelar_txt),
            command=self.on_cancelar,
            bootstyle=BTN_VERMELHO,
            )

        btn_calcular_txt = "Calcular"
        btn_calcular = ttkbs.Button(
            master=container,
            text=btn_calcular_txt,
            width=len(btn_calcular_txt),
            command=self.on_calcular,
            bootstyle=BTN_VERDE,
            )
        
        btn_calcular.pack(side=DIREITA, padx=5)
        btn_cancelar.pack(side=DIREITA, padx=5)

        btn_calcular.focus_set()

    def criar_form(self, titulo: str, variavel: ttkbs.StringVar) -> None:
        container = ttkbs.Frame(self)
        container.pack(
            fill=HORIZONTAL,
            expand=SIM,
            pady=5)

        elemento_txt = ttkbs.Label(master=container, text=titulo.title(), width=10)
        elemento_input = ttkbs.Entry(master=container, textvariable=variavel)
        
        elemento_txt.pack(
            side=ESQUERDA,
            padx=5)

        elemento_input.pack(
            side=ESQUERDA,
            fill=HORIZONTAL,
            expand=SIM,
            padx=4)


class App:
    def __init__(self) -> None:
        app = ttkbs.Window(
            title="App: Cálculo Mol",
            themename="superhero",
            resizable=(0, 0)
            )
        InterfaceTkBS(app)
        app.mainloop()


if __name__ == "__main__":
    pass