
from math import ceil

from .trabalho import Trabalho
from ..ferramentas import pegarPagina, emPaginasDe


class Caderno(Trabalho):
    def __init__(self, caderno, **kwargs):
        super().__init__(**kwargs)

        self.caderno            = caderno
        self.paineis['caderno'] = caderno
        self.pagina_atual       = 0
        self.pagina_total       = 0

        self.caderno.botoes['+'].comando = self.adicionarRef
        self.caderno.botoes['-'].comando = self.subtrairRef
        self.caderno.botoes['<<'].comando = self.paginacaoAnterior
        self.caderno.botoes['>>'].comando = self.paginacaoProxima


    def adicionarRef(self):
        self.sistema.area_trabalho = 'referencias'


    def subtrairRef(self):
        if self.sistema.refe_selecionada == None:
            return

        self.sistema.lista_referencias.remove(self.sistema.refe_selecionada)
        self.resetSelecao()
        self.configPaginacao()


    def paginacaoAnterior(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
            self.caderno.setPaginacao(self.pagina_atual, self.pagina_total)


    def paginacaoProxima(self):
        if self.pagina_atual < self.pagina_total:
            self.pagina_atual += 1
            self.caderno.setPaginacao(self.pagina_atual, self.pagina_total)


    def configPaginacao(self):
        self.pagina_total = ceil(len(self.sistema.lista_referencias) / 6)
        self.pagina_atual = self.pagina_total
        self.caderno.setPaginacao(self.pagina_atual, self.pagina_total)

        for pagina in emPaginasDe(self.sistema.lista_referencias, 6):
            for interface, pos_y in zip(pagina, self.caderno.render_pontos):
                interface.painel.render_pos = (interface.painel.render_pos[0], pos_y)

                for botao in interface.painel.botoes.values():
                    botao.rect_click.y  = pos_y


    def eventos(self, evento):
        if super().eventos(evento):
            return

        for interface in pegarPagina(self.sistema.lista_referencias, 6, self.pagina_atual):
            for botao in interface.painel.botoes.values():
                if botao.click(evento):
                    return


    def draw(self):
        super().draw()

        for interface in pegarPagina(self.sistema.lista_referencias, 6, self.pagina_atual):
            interface.draw()

