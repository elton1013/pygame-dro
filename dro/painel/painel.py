import pygame

from .. import elementos


##Base
class Painel:
    gap = 5

    def __init__(self, root, **kwargs):
        self.root       = root
        self.surface    = pygame.Surface(self.tamanho)
        self.botoes     = {}

        self.painelConfig()
        self.botoesConfig()
        self.renderImg()

    def painelConfig(self): pass
    def botoesConfig(self): pass

    def renderImg(self):
        self.surface.fill(elementos.Cores.FUNDO)

        for botao in self.botoes.values():
            botao.draw(self.surface)


    def draw(self):
        self.root.blit(self.surface, self.render_pos)

