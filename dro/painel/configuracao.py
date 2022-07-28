import pygame

from .. import elementos
from  .painel import Painel as Painel


class Configuracao(Painel):
    def __init__(self, **kwargs):
        self.tamanho = (640, 480 - 60)
        self.render_pos = (0, 60)

        super().__init__(**kwargs)

        self.setEtiquetaPrecisaoX()
        self.setEtiquetaPrecisaoY()


    def painelConfig(self):
        self.rect_painel = pygame.Rect(
                self.gap,
                self.gap,
                self.tamanho[0] - 2 * self.gap,
                200)

        self.titulo     = elementos.fonte_botao.render('Precisão')
        self.titulo_pos = (self.gap + self.rect_painel.x,
                           self.gap + self.rect_painel.y)

        self.etiqueta_precisao_x_pos = (130 + self.render_pos[0],
                                        self.titulo_pos[1] + self.render_pos[1] + 60)

        self.etiqueta_precisao_y_pos = (130 + self.render_pos[0],
                                        self.titulo_pos[1] + self.render_pos[1] + 140)


    def botoesConfig(self):
        config = {
                'x'       : self.rect_painel.x + self.gap,
                'largura' : 100,
                'altura'  : 60,
                'desloc'  : self.render_pos,
                }

        self.botoes['Precisao X'] = elementos.Botao(
                y     = 50,
                texto = 'x',
                **config)

        self.botoes['Precisao Y'] = elementos.Botao(
                y     = 130,
                texto = 'y',
                **config)


    def setEtiquetaPrecisaoX(self, precisao = 0):
        self.etiqueta_precisao_x = elementos.fonte_botao.render(f'{precisao}')


    def setEtiquetaPrecisaoY(self, precisao = 0):
        self.etiqueta_precisao_y = elementos.fonte_botao.render(f'{precisao}')


    def renderImg(self):
        super().renderImg()
        pygame.draw.rect(self.surface, elementos.Cores.FONTE, self.rect_painel, 1)
        self.surface.blit(self.titulo, self.titulo_pos)


    def draw(self):
        self.root.blit(self.surface, self.render_pos)
        self.root.blit(self.etiqueta_precisao_x, self.etiqueta_precisao_x_pos)
        self.root.blit(self.etiqueta_precisao_y, self.etiqueta_precisao_y_pos)

