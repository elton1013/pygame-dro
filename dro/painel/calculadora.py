import pygame

from .. import elementos
from  .painel import Painel as Painel


class Calculadora(Painel):
    def __init__(self, **kwargs):
        self.tamanho    = (640, 480)
        self.render_pos = (0, 0)
        self.setEtiqueta()
        self.setDisplay()

        super().__init__(**kwargs)



    def painelConfig(self):
        self.display_pos = (20, 20)


    def botoesConfig(self):
        config = {
                'largura'  : 100,
                'altura'   : 80,
                'desloc_y' : 100,
                }

        linhas = [
                ['Cancelar' , '7', '8', '9' , '(', ')'],
                ['Limpar'   , '4', '5', '6' , '*', '/'],
                ['Back'     , '1', '2', '3' , '+', '-'],
                ['Get'      , '0', '.', 'pi', '=', 'Set'],
                ]

        for pos_y, linha in enumerate(linhas):
            for pos_x, tecla in enumerate(linha):
                self.botoes[tecla] = elementos.Botao(
                        x = self.gap + pos_x * (config['largura'] + self.gap),
                        y = pos_y * (config['altura']  + self.gap) + config['desloc_y'],
                        texto = tecla,
                        **config)


    def setEtiqueta(self, etiqueta = '*'):
        self.etiqueta = etiqueta


    def setDisplay(self, valor = ''):
        self.display = elementos.fonte_calculadora.render(f'{self.etiqueta} : {valor}')


    def draw(self):
        self.root.blit(self.surface, self.render_pos)
        self.root.blit(self.display, self.display_pos)
