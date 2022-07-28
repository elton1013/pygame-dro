
from ..painel.referencia import (
        Refe as PainelRefe,
        Modo as PainelModo,)

from .modificador import (
        ModificadorFurosAoRaio,
        ModificadorFurosADiagonal,)


class Refe:
    def __init__(self, sistema, etiqueta, etiqueta_final, pos, tipo, **kwargs):
        self.sistema      = sistema
        self.tipo           = tipo
        self.etiqueta       = etiqueta
        self.pos            = pos
        self.etiqueta_final = etiqueta_final
        self.painel         = PainelRefe(etiqueta = etiqueta_final, tamanho = self.sistema.tamanho, root = self.sistema.root)
        self.coord_x        = self.sistema.sensor.leitura[0]
        self.coord_y        = self.sistema.sensor.leitura[1]

        self.painel.botoes['Set'].comando = self.set


    def set(self):
        self.sistema.paineis['trabalho'].setEtiqueta(self.etiqueta_final)
        self.sistema.refe_selecionada = self

        if 'X' in self.tipo:
            self.sistema.ajuste_x = self.coord_x

        if 'Y' in self.tipo:
            self.sistema.ajuste_y = self.coord_y


    def draw(self):
        if self.sistema.refe_selecionada == self:
            self.painel.drawSelect()
            return

        self.painel.draw()


##Modo
class Modo(Refe):
    def __init__(self, sistema, etiqueta, etiqueta_final, pos, **kwargs):
        super().__init__(sistema, etiqueta, etiqueta_final, pos, **kwargs)
        self.painel = PainelModo(etiqueta = etiqueta_final, tamanho = self.sistema.tamanho, root = self.sistema.root)

        self.painel.botoes['Set'].comando = self.set
        self.painel.botoes['Enter'].comando = self.enter


        if 'Mod Raio' == etiqueta:
            self.modificador = ModificadorFurosAoRaio(
                    **sistema.paineis,
                    sistema       = sistema,
                    area_trabalho = 'modificador',
                    etiqueta      = etiqueta_final,
                    coord_x       = self.coord_x,
                    coord_y       = self.coord_y,
                    **kwargs)

        elif 'Mod Diagl' == etiqueta:
            self.modificador = ModificadorFurosADiagonal(
                    **sistema.paineis,
                    sistema       = sistema,
                    area_trabalho = 'modificador',
                    etiqueta      = etiqueta_final,
                    coord_x       = self.coord_x,
                    coord_y       = self.coord_y,
                    **kwargs)


    def enter(self):
        self.sistema.area_trabalho = 'modificador'
        self.sistema.interfaces['modificador'] = self.modificador
        self.modificador.reDraw()

