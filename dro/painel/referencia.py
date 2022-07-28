import pygame

from .. import elementos
from  .painel import Painel as Painel


class Refe(Painel):
    def __init__(self, etiqueta, **kwargs):
        self.tamanho        = (386, 65)
        self.surface_select = pygame.Surface(self.tamanho)
        self.render_pos     = (self.gap + 2, 0)
        self.etiqueta       = etiqueta
        self.texto          = elementos.fonte_botao.render(self.etiqueta)

        super().__init__(**kwargs)


    def painelConfig(self):
        self.rect_painel = pygame.Rect(
                0,
                0,
                *self.tamanho)

        self.etiqueta_pos = (
                self.rect_painel.x + 100,
                self.rect_painel.y + 20)


    def botoesConfig(self):
        config = {
                'largura' : 80,
                'altura'  : 54,
                'desloc'  : self.render_pos,
                'texto'   : 'Set',
                }

        self.botoes['Set'] = elementos.Botao(
                x = self.rect_painel.x + self.gap,
                y = self.gap,
                **config)


    def renderImg(self):
        #select
        self.surface_select.fill(elementos.Cores.VERDE)
        pygame.draw.rect(self.surface_select, elementos.Cores.FONTE, self.rect_painel, 1)
        self.surface_select.blit(self.texto, self.etiqueta_pos)

        for botao in self.botoes.values():
            botao.draw(self.surface_select)

        #normal
        self.surface.fill(elementos.Cores.FUNDO)
        pygame.draw.rect(self.surface, elementos.Cores.FONTE, self.rect_painel, 1)
        self.surface.blit(self.texto, self.etiqueta_pos)

        for botao in self.botoes.values():
            botao.draw(self.surface)

    
    def drawSelect(self):
        self.root.blit(self.surface_select, self.render_pos)


###

class Modo(Refe):
    def botoesConfig(self):
        super().botoesConfig()
        config = {
                'largura' : 80,
                'altura'  : 54,
                'desloc'  : self.render_pos,
                'texto'   : 'Enter',
                }

        self.botoes['Enter'] = elementos.Botao(
                x = self.rect_painel.right - config['largura'] - self.gap,
                y = self.gap,
                **config)

