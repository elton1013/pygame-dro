import pygame

from .. import elementos
from  .painel import Painel as Painel


class ListaReferencias(Painel):
    def __init__(self, **kwargs):
        self.tamanho    = (400, 480)
        self.render_pos = (0, 0)

        super().__init__(**kwargs)


    def painelConfig(self):
        self.rect_painel = pygame.Rect(
                self.gap,
                self.gap,
                self.tamanho[0] - 2 * self.gap,
                self.tamanho[1] - 2 * self.gap)


    def botoesConfig(self):
        config = {
                'largura' : 123,
                'altura'  : 76,
                'desloc'  : self.render_pos,
                }

        lista = (('Origem', 'Referencia', 'Furo'),
                 ('Centro', 'Centro X', 'Centro Y'),
                 ('X',   'Y'),
                 ('Borda X',   'Borda Y'),
                 ('Mod Raio', 'Mod Diagl'),
                 )

        for pos_y, linha in enumerate(lista):
            for pos_x, texto in enumerate(linha):
                self.botoes[texto] = elementos.Botao(
                        x = self.rect_painel.x + self.gap + (self.gap + config['largura']) * pos_x,
                        y = self.rect_painel.y + self.gap + (self.gap + config['altura'])  * pos_y,
                        texto = texto,
                        **config)


    def renderImg(self):
        super().renderImg()
        pygame.draw.rect(self.surface, elementos.Cores.FONTE, self.rect_painel, 1)

