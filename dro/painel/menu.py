import pygame

from .. import elementos
from  .painel import Painel as Painel


##Base
class Menu(Painel):
    lista_de_botoes = ()

    def __init__(self, **kwargs):
        self.tamanho    = (640, 60)
        self.render_pos = (0, 0)
        super().__init__(**kwargs)


    def botoesConfig(self):
        config = {
                'y'       : self.gap,
                'largura' : 140,
                'altura'  : 50,
                'desloc'  : self.render_pos,
                }

        for pos, texto in enumerate(self.lista_de_botoes):
            self.botoes[texto] = elementos.Botao(
                    x     = self.gap + pos * (config['largura'] + self.gap),
                    texto = texto,
                    **config)



class MenuTrabalho(Menu):
    lista_de_botoes = ('Configurar',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tamanho    = (240, 60)
        self.surface    = pygame.Surface(self.tamanho)
        self.render_pos = (640 - self.tamanho[0], 0)

        self.painelConfig()
        self.botoesConfig()
        self.renderImg()


class MenuConfiguracao(Menu):
    lista_de_botoes = ('Salvar', 'Voltar', 'Fechar', 'Desligar')

