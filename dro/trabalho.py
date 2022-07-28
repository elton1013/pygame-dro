import pygame

from .. import elementos
from  .painel import Painel as Painel


class Trabalho(Painel):
    def __init__(self, **kwargs):
        self.tamanho    = (240, 420)
        self.render_pos = (640 - self.tamanho[0],
                           480 - self.tamanho[1])

        super().__init__(**kwargs)

        self.setEtiqueta()
        self.setCoord(0, 0)


    def painelConfig(self):
        self.rect_display = pygame.Rect(
                self.gap,
                self.gap,
                self.tamanho[0] - 2 * self.gap,
                160)

        self.etiqueta_ref_pos = (self.render_pos[0] + self.rect_display.x + self.gap,
                                 self.render_pos[1] + self.rect_display.y + self.gap)

        self.etiqueta_eixo_x     = elementos.fonte_botao.render('x')
        self.etiqueta_eixo_x_pos = (self.rect_display.x + self.gap,
                                    self.rect_display.y + 55)

        self.etiqueta_eixo_y     = elementos.fonte_botao.render('y')
        self.etiqueta_eixo_y_pos = (self.rect_display.x + self.gap,
                                    self.rect_display.y + 115)

        self.coord_x_pos = (self.render_pos[0] + self.rect_display.right - self.gap,
                            self.render_pos[1] + self.etiqueta_eixo_x_pos[1] - 15)

        self.coord_y_pos = (self.render_pos[0] + self.rect_display.right - self.gap,
                            self.render_pos[1] + self.etiqueta_eixo_y_pos[1] - 15)


    def botoesConfig(self):
        config = {
                'largura' : 112,
                'altura'  : 78,
                'desloc'  : self.render_pos,
                }

        lista = (('X Zero','Y Zero'),
                 ('X 1/2' ,'Y 1/2'),
                 ('X Calc','Y Calc'))

        for pos, texto in enumerate(lista):
            self.botoes[texto[0]] = elementos.Botao(
                    x      = self.gap,
                    y      = (config['altura'] + self.gap) * pos + self.rect_display.bottom + self.gap,
                    texto  = texto[0],
                    **config)

            self.botoes[texto[1]] = elementos.Botao(
                    x     = self.rect_display.right - config['largura'],
                    y     = (config['altura'] + self.gap) * pos + self.rect_display.bottom + self.gap,
                    texto = texto[1],
                    **config)


    def setEtiqueta(self, etiqueta = '*'):
        self.etiqueta_ref = elementos.fonte_botao.render(etiqueta)


    def setCoord(self, x, y):
        self.coord_x = elementos.fonte_coordenada.render(f'{x:0.3f}')
        self.coord_y = elementos.fonte_coordenada.render(f'{y:0.3f}')


    def renderCoord(self):
        self.root.blit(self.coord_x,
                (self.coord_x_pos[0] - self.coord_x.get_width(),
                 self.coord_x_pos[1]))

        self.root.blit(self.coord_y,
                (self.coord_y_pos[0] - self.coord_y.get_width(),
                 self.coord_y_pos[1]))


    def renderImg(self):
        self.surface.fill(elementos.Cores.FUNDO)
        pygame.draw.rect(self.surface, elementos.Cores.FONTE, self.rect_display, 1)
        self.surface.blit(self.etiqueta_eixo_x, self.etiqueta_eixo_x_pos)
        self.surface.blit(self.etiqueta_eixo_y, self.etiqueta_eixo_y_pos)

        for botao in self.botoes.values():
            botao.draw(self.surface)


    def draw(self):
        self.root.blit(self.surface, self.render_pos)
        self.root.blit(self.etiqueta_ref, self.etiqueta_ref_pos)
        self.renderCoord()

