import pygame
pygame.font.init()


class Cores:
    FONTE = (238, 238, 238)
    FUNDO = (49, 49, 49)
    BOTAO = (89, 89, 89)
    VERDE = (33, 115, 70)
    VERDE = (3, 85, 40)
    PRETO = (0, 0, 0)



class Font:
    def __init__(self, tamanho, cor):
        self.cor     = cor
        self.font    = pygame.font.SysFont('DejaVu Sans', tamanho)


    def render(self, texto, background=None):
        return self.font.render(texto, True, self.cor, background)


fonte_coordenada  = Font(44, Cores.FONTE)
fonte_calculadora = Font(30, Cores.FONTE)
fonte_botao       = Font(20, Cores.FONTE)



class Botao:
    def __init__(self, x, y, largura, altura, texto, desloc=(0, 0), **kwargs):
        self.rect_render = pygame.Rect(x, y, largura, altura)
        self.rect_click  = pygame.Rect(x + desloc[0], y + desloc[1], largura, altura)

        self.texto     = fonte_botao.render(texto)
        self.texto_pos = (self.rect_render.centerx - (self.texto.get_width()/2),
                          self.rect_render.centery - (self.texto.get_height()/2))


    def click(self, event):
        if self.rect_click.collidepoint(event.pos):
            self.comando()
            return 1


    def comando(self):
        print('Comando não definido para botão!')


    def draw(self, tela):
        pygame.draw.rect(tela, Cores.BOTAO, self.rect_render)
        tela.blit(self.texto, self.texto_pos)

