import pygame

from .. import elementos
from  .painel import Painel as Painel


class Caderno(Painel):
    botao_func = ('-', '+')

    def __init__(self, **kwargs):
        self.tamanho    = (400, 420)
        self.render_pos = (0, 60)
        super().__init__(**kwargs)

        self.setPaginacao()


    def painelConfig(self):
        self.painel_rect = pygame.Rect(
                self.gap,
                self.gap,
                self.tamanho[0] - 2 * self.gap,
                338)

        self.render_pontos = [
                self.render_pos[1] + 2 + self.gap + y * 67
                for y in
                range(0, 5)
                ]


    def botoesConfig(self):
        config = {
                'largura' : 76,
                'altura'  : 65,
                'desloc'  : self.render_pos,
                'y'       : self.painel_rect.bottom + self.gap,
                }

        self.botoes['<<'] = elementos.Botao(
                x     = self.gap,
                texto = '<<',
                **config)

        self.botoes['>>'] = elementos.Botao(
                x     = self.painel_rect.right - 2 * self.gap - 3 * config['largura'],
                texto = '>>',
                **config)

        self.botoes[self.botao_func[0]] = elementos.Botao(
                x     = self.painel_rect.right - self.gap - 2 * config['largura'],
                texto = self.botao_func[0],
                **config)

        self.botoes[self.botao_func[1]] = elementos.Botao(
                x     = self.painel_rect.right - config['largura'],
                texto = self.botao_func[1],
                **config)

        rect_anterior = self.botoes['<<'].rect_render
        rect_proximo  = self.botoes['>>'].rect_render
        self.paginacao_pos = (
                (rect_proximo.left - rect_anterior.right) /2 + rect_anterior.right + self.render_pos[0],
                rect_anterior.centery + self.render_pos[1])


    def setPaginacao(self, atual=0, total=0):
        self.paginacao = elementos.fonte_botao.render(f'{atual}/{total}')


    def renderPaginacao(self):
        r = self.paginacao.get_rect()
        r.center = self.paginacao_pos
        self.root.blit(self.paginacao, r)


    def renderImg(self):
        super().renderImg()
        pygame.draw.rect(self.surface, elementos.Cores.FONTE, self.painel_rect, 1)


    def draw(self):
        self.root.blit(self.surface, self.render_pos)
        self.renderPaginacao()


###
class Modificador(Caderno):
    botao_func = ('Calc', 'Voltar')
    variaveis = {}

    def __init__(self, etiqueta, **kwargs):
        self.etiqueta_refe = elementos.fonte_botao.render(etiqueta)

        super().__init__(**kwargs)
        self.entradasConfig()
        self.renderVariaveis()
        self.renderImg()


    def painelConfig(self):
        self.painel_rect = pygame.Rect(
                self.gap,
                self.gap,
                self.tamanho[0] - 2 * self.gap,
                338)

        self.etiqueta_refe_pos = (2 * self.gap, 2 * self.gap)


    def entradasConfig(self):
        config = {
                'largura' : 100,
                'altura'  : 60,
                'desloc'  : self.render_pos,
                'x'       : self.painel_rect.x + self.gap,
                }


        for pos, variavel in enumerate(self.variaveis.values()):
            pos_y = self.painel_rect.y + config['altura'] + pos * (config['altura'] + self.gap)

            self.botoes[variavel['nome']] = elementos.Botao(
                    y     = pos_y,
                    texto = variavel['nome'],
                    **config)

            b_rect = self.botoes[variavel['nome']].rect_render
            variavel['pos'] = (b_rect.right + self.render_pos[0] + 4 * self.gap,
                               pos_y + self.render_pos[1] + 4 * self.gap),
            variavel['img'] = elementos.fonte_botao.render(variavel['formato'] % 0)


    def setVariavel(self, variavel, valor=0):
        self.variaveis[variavel]['img'] = elementos.fonte_botao.render(self.variaveis[variavel]['formato'] % valor)


    def renderVariaveis(self):
        for variavel in  self.variaveis.values():
            self.root.blit(variavel['img'], variavel['pos'])


    def renderImg(self):
        super().renderImg()
        self.surface.blit(self.etiqueta_refe, self.etiqueta_refe_pos)


    def draw(self):
        super().draw()
        self.renderVariaveis()



class ModificadorFurosAoRaio(Modificador):
    variaveis = {
            'furos'  : {'nome' : 'furos',  'formato' : '%d',    'img' : None, 'pos' : (0, 0)},
            'raio'   : {'nome' : 'raio',   'formato' : '%.2f',  'img' : None, 'pos' : (0, 0)},
            'desloc' : {'nome' : 'desloc', 'formato' : '%.2f°', 'img' : None, 'pos' : (0, 0)},
            }


class ModificadorFurosADiagonal(Modificador):
    variaveis = {
            'furos'  : {'nome' : 'furos',  'formato' : '%d',    'img' : None, 'pos' : (0, 0)},
            'angulo' : {'nome' : 'angulo', 'formato' : '%.2f°', 'img' : None, 'pos' : (0, 0)},
            'espaco' : {'nome' : 'espaço', 'formato' : '%.2f',  'img' : None, 'pos' : (0, 0)},
            'desloc' : {'nome' : 'desloc', 'formato' : '%.2f',  'img' : None, 'pos' : (0, 0)},
            }

