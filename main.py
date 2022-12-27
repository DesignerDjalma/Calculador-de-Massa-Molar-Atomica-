from funcoes import calcular_massa_molar_de_elemento
import ttkbootstrap

ESQUERDA = ttkbootstrap.constants.LEFT
AMBOS = ttkbootstrap.constants.BOTH
HORIZONTAL = ttkbootstrap.constants.X


class InterfaceTkBS(ttkbootstrap.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=AMBOS,
            expand=ttkbootstrap.constants.YES,)

        self.elemento_quimico = ttkbootstrap.StringVar(value="")

        info_txt = "Forneça um Elemento da Tabela Periódica"
        info = ttkbootstrap.Label(master=self, text=info_txt, width=len(info_txt))
        info.pack(fill=HORIZONTAL, pady=10)

        self.criar_form("Sigla", self.elemento_quimico)
        self.criar_caixa_botoes()

        self.resultado_txt = ttkbootstrap.StringVar(value="Resultado: ")
        self.resultado = ttkbootstrap.Label(
            master=self,
            textvariable=self.resultado_txt,
            width=30,
            )
        self.resultado.pack(fill=HORIZONTAL, pady=10)


    def on_calcular(self) -> None:
        res = calcular_massa_molar_de_elemento(self.elemento_quimico.get())
        print(res)
        self.resultado_txt.set(f"Resultado: {res}")

    def on_cancelar(self) -> None:
        pass

    def on_cancelar(self) -> None:
        pass

    def criar_caixa_botoes(self) -> None:
        container = ttkbootstrap.Frame(self)
        container.pack(
            fill=HORIZONTAL,
            expand=ttkbootstrap.constants.YES,
            pady=(15, 10))

        btn_cancelar_txt = "Cancelar"
        btn_cancelar = ttkbootstrap.Button(
            master=container,
            text=btn_cancelar_txt,
            width=len(btn_cancelar_txt),
            command=self.on_cancelar,
            bootstyle=ttkbootstrap.constants.DANGER,
            )

        btn_calcular_txt = "Calcular"
        btn_calcular = ttkbootstrap.Button(
            master=container,
            text=btn_calcular_txt,
            width=len(btn_calcular_txt),
            command=self.on_calcular,
            bootstyle=ttkbootstrap.constants.SUCCESS,
            )
        
        btn_calcular.pack(side=ttkbootstrap.constants.RIGHT, padx=5)
        btn_cancelar.pack(side=ttkbootstrap.constants.RIGHT, padx=5)

        btn_calcular.focus_set()

    def criar_form(self, titulo: str, variavel: ttkbootstrap.StringVar) -> None:
        container = ttkbootstrap.Frame(self)
        container.pack(
            fill=HORIZONTAL,
            expand=ttkbootstrap.constants.YES,
            pady=5)

        elemento_txt = ttkbootstrap.Label(master=container, text=titulo.title(), width=10)
        elemento_input = ttkbootstrap.Entry(master=container, textvariable=variavel)
        
        elemento_txt.pack(
            side=ESQUERDA,
            padx=5)

        elemento_input.pack(
            side=ESQUERDA,
            fill=HORIZONTAL,
            expand=ttkbootstrap.constants.YES,
            padx=4)


if __name__ == "__main__":

    app = ttkbootstrap.Window(
        title="App: Cálculo Mol",
        themename="superhero",
        resizable=(0, 0)
        )

    InterfaceTkBS(app)
    app.mainloop()