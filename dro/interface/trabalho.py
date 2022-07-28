
from .menu import MenuTrabalho


class Trabalho(MenuTrabalho):
    def __init__(self, trabalho, **kwargs):
        super().__init__(**kwargs)

        self.trabalho            = trabalho
        self.paineis['trabalho'] = trabalho

        self.trabalho.botoes['X Zero'].comando = self.zerarX
        self.trabalho.botoes['Y Zero'].comando = self.zerarY
        self.trabalho.botoes['X 1/2'].comando  = self.centroX
        self.trabalho.botoes['Y 1/2'].comando  = self.centroY
        self.trabalho.botoes['X Calc'].comando = self.calcX
        self.trabalho.botoes['Y Calc'].comando = self.calcY


    def zerarX(self):
        self.sistema.ajuste_x = self.sistema.sensor.leitura[0]
        self.resetSelecao()


    def zerarY(self):
        self.sistema.ajuste_y = self.sistema.sensor.leitura[1]
        self.resetSelecao()


    def centroX(self):
        self.sistema.ajuste_x += round(
                (self.sistema.sensor.leitura[0] - self.sistema.ajuste_x) / 2
                )
        self.resetSelecao()


    def centroY(self):
        self.sistema.ajuste_y += round(
                (self.sistema.sensor.leitura[1] - self.sistema.ajuste_y) / 2
                )
        self.resetSelecao()


    def calcX(self):
        self.interface_calculadora.chamar(
                var            = str(self.sistema.converterSinal()[0]),
                etiqueta       = 'x',
                funcao_retorno = self.calcRetornoX,
                pegar_variavel = self.pegarX,
                )


    def calcY(self):
        self.interface_calculadora.chamar(
                var            = str(self.sistema.converterSinal()[1]),
                etiqueta       = 'y',
                funcao_retorno = self.calcRetornoY,
                pegar_variavel = self.pegarY,
                )

    def calcRetornoX(self, valor):
        self.sistema.ajuste_x = round(
                self.sistema.sensor.leitura[0] - float(valor) / self.sistema.precisao_x
                )
        self.resetSelecao()


    def calcRetornoY(self, valor):
        self.sistema.ajuste_y = round(
                self.sistema.sensor.leitura[1] - float(valor) / self.sistema.precisao_y
                )
        self.resetSelecao()


    def pegarX(self):
        return self.sistema.converterSinal()[0]


    def pegarY(self):
        return self.sistema.converterSinal()[1]


    def resetSelecao(self):
        self.trabalho.setEtiqueta()
        self.sistema.refe_selecionada = None


    def rotina(self):
        super().rotina()
        self.trabalho.setCoord(*self.sistema.converterSinal())

