
from .menu import MenuConfig


class Configuracao(MenuConfig):
    def __init__(self, configuracao, **kwargs):
        super().__init__(**kwargs)

        self.configuracao            = configuracao
        self.paineis['configuracao'] = configuracao

        self.configuracao.setEtiquetaPrecisaoX(self.sistema.precisao_x)
        self.configuracao.setEtiquetaPrecisaoY(self.sistema.precisao_y)

        self.configuracao.botoes['Precisao X'].comando = self.calcPrecisaoX
        self.configuracao.botoes['Precisao Y'].comando = self.calcPrecisaoY


    def calcPrecisaoX(self):
        self.interface_calculadora.chamar(
                var            = str(self.sistema.precisao_x),
                etiqueta       = 'x',
                funcao_retorno = self.calcPrecisaoRetornoX,
                pegar_variavel = self.pegarPrecisaoX,
                )


    def calcPrecisaoY(self):
        self.interface_calculadora.chamar(
                var            = str(self.sistema.precisao_y),
                etiqueta       = 'y',
                funcao_retorno = self.calcPrecisaoRetornoY,
                pegar_variavel = self.pegarPrecisaoY,
                )


    def calcPrecisaoRetornoX(self, arg):
        self.configuracao.setEtiquetaPrecisaoX(arg)
        self.sistema.precisao_x = float(arg)


    def calcPrecisaoRetornoY(self, arg):
        self.configuracao.setEtiquetaPrecisaoY(arg)
        self.sistema.precisao_y = float(arg)


    def pegarPrecisaoX(self):
        return self.sistema.precisao_x


    def pegarPrecisaoY(self):
        return self.sistema.precisao_y

