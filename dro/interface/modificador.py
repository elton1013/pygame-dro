
from ..ferramentas import calcFurosAoRaio, calcFurosADiagonal

from ..painel.caderno import (
        ModificadorFurosAoRaio    as PainelModificadorFurosAoRaio,
        ModificadorFurosADiagonal as PainelModificadorFurosADiagonal,)

from .trabalho import Trabalho


class Modificador(Trabalho):
    def __init__(self, etiqueta, coord_x, coord_y, **kwargs):
        super().__init__(**kwargs)
        self.interface_calculadora = self.sistema.interfaces['calculadora']

        self.coord_x      = coord_x
        self.coord_y      = coord_y
        self.etiqueta_mod = etiqueta
        self.coordenadas  = ()

        self.pagina_atual = 0
        self.pagina_total = 0

        self.painel.botoes['Voltar'].comando = self.voltar
        self.painel.botoes['<<'].comando = self.furoAnterior
        self.painel.botoes['>>'].comando = self.furoProximo


    def voltar(self):
        self.sistema.area_trabalho = 'trabalho'


    def furoAnterior(self):
        if not self.coordenadas:
            return

        self.pagina_atual -= 1
        if self.pagina_atual < 0:
            self.pagina_atual = len(self.coordenadas) - 1

        self.setPaginacao()


    def furoProximo(self):
        if not self.coordenadas:
            return

        self.pagina_atual += 1
        if self.pagina_atual >= len(self.coordenadas):
            self.pagina_atual = 0

        self.setPaginacao()


    def setPaginacao(self):
        self.painel.setPaginacao(self.pagina_atual + 1, self.pagina_total)
        self.sistema.paineis['trabalho'].setEtiqueta(f'{self.etiqueta_mod} - furo {self.pagina_atual + 1:02d}')
        self.sistema.ajuste_x = self.coordenadas[self.pagina_atual][0]
        self.sistema.ajuste_y = self.coordenadas[self.pagina_atual][1]
        self.sistema.refe_selecionada = None


##painelmodo
class ModificadorFurosAoRaio(Modificador):
    def __init__(self, etiqueta, sistema, **kwargs):
        self.painel = PainelModificadorFurosAoRaio(
                root     = sistema.root,
                tamanho  = sistema.tamanho,
                etiqueta = etiqueta)
        super().__init__(etiqueta = 'Ao Raio', sistema = sistema, **kwargs)

        self.paineis['modificador'] = self.painel

        self.furos  = 0
        self.raio   = 0
        self.desloc = 0

        self.painel.botoes['furos'].comando  = self.calcFuros
        self.painel.botoes['raio'].comando   = self.calcRaio
        self.painel.botoes['desloc'].comando = self.calcDesloc
        self.painel.botoes['Calc'].comando = self.calcFurosAoRaio


    ###atualiza variaveis na exibição
    def reDraw(self):
        self.painel.setVariavel('furos',  self.furos)
        self.painel.setVariavel('raio',   self.raio)
        self.painel.setVariavel('desloc', self.desloc)


    ###furos
    def calcFuros(self):
        self.interface_calculadora.chamar(
                var            = str(self.furos),
                etiqueta       = 'furos',
                funcao_retorno = self.calcFurosRetorno,
                pegar_variavel = self.pegarFuros,
                )


    def calcFurosRetorno(self, valor):
        self.furos = int(valor)
        self.painel.setVariavel('furos', self.furos)


    def pegarFuros(self):
        return self.furos

    ###furos

    ###raio
    def calcRaio(self):
        self.interface_calculadora.chamar(
                var            = str(self.raio),
                etiqueta       = 'raio',
                funcao_retorno = self.calcRaioRetorno,
                pegar_variavel = self.pegarRaio,
                )


    def calcRaioRetorno(self, valor):
        self.raio = int(valor)
        self.painel.setVariavel('raio', self.raio)


    def pegarRaio(self):
        return self.raio

    ###raio

    ###desloc
    def calcDesloc(self):
        self.interface_calculadora.chamar(
                var            = str(self.desloc),
                etiqueta       = 'desloc',
                funcao_retorno = self.calcDeslocRetorno,
                pegar_variavel = self.pegarDesloc,
                )


    def calcDeslocRetorno(self, valor):
        self.desloc = int(valor)
        self.painel.setVariavel('desloc', self.desloc)


    def pegarDesloc(self):
        return self.desloc

    ###desloc

    ###calc
    def calcFurosAoRaio(self):
        if self.furos < 1: return
        if self.raio  < 1: return

        self.coordenadas = [
                (self.sistema.converterParaPassoX(x) + self.coord_x,
                 self.sistema.converterParaPassoY(y) + self.coord_y)
                for x, y in
                calcFurosAoRaio(self.furos, self.raio, self.desloc)]
        
        self.pagina_total = 0
        self.pagina_total = len(self.coordenadas)

        self.setPaginacao()


class ModificadorFurosADiagonal(Modificador):
    def __init__(self, etiqueta, sistema, **kwargs):
        self.painel = PainelModificadorFurosADiagonal(
                root     = sistema.root,
                tamanho  = sistema.tamanho,
                etiqueta = etiqueta)
        super().__init__(etiqueta = 'Diagl', sistema = sistema, **kwargs)

        self.paineis['modificador'] = self.painel

        self.furos  = 0
        self.angulo = 0
        self.espaco = 0
        self.desloc = 0

        self.painel.botoes['furos'].comando  = self.calcFuros
        self.painel.botoes['angulo'].comando = self.calcAngulo
        self.painel.botoes['espaço'].comando = self.calcEspaco
        self.painel.botoes['desloc'].comando = self.calcDesloc
        self.painel.botoes['Calc'].comando = self.calcFurosADiagonal


    ###atualiza variaveis na exibição
    def reDraw(self):
        self.painel.setVariavel('furos',  self.furos)
        self.painel.setVariavel('angulo', self.angulo)
        self.painel.setVariavel('espaco', self.espaco)
        self.painel.setVariavel('desloc', self.desloc)


    ###furos
    def calcFuros(self):
        self.interface_calculadora.chamar(
                var            = str(self.furos),
                etiqueta       = 'furos',
                funcao_retorno = self.calcFurosRetorno,
                pegar_variavel = self.pegarFuros,
                )


    def calcFurosRetorno(self, valor):
        self.furos = int(valor)
        self.painel.setVariavel('furos', self.furos)


    def pegarFuros(self):
        return self.furos

    ###furos

    ###angulo
    def calcAngulo(self):
        self.interface_calculadora.chamar(
                var            = str(self.angulo),
                etiqueta       = 'angulo',
                funcao_retorno = self.calcAnguloRetorno,
                pegar_variavel = self.pegarAngulo,
                )


    def calcAnguloRetorno(self, valor):
        self.angulo = int(valor)
        self.painel.setVariavel('angulo', self.angulo)


    def pegarAngulo(self):
        return self.angulo

    ###angulo

    ###espaco
    def calcEspaco(self):
        self.interface_calculadora.chamar(
                var            = str(self.espaco),
                etiqueta       = 'espaço',
                funcao_retorno = self.calcEspacoRetorno,
                pegar_variavel = self.pegarEspaco,
                )


    def calcEspacoRetorno(self, valor):
        self.espaco = int(valor)
        self.painel.setVariavel('espaco', self.espaco)


    def pegarEspaco(self):
        return self.espaco

    ###espaco

    ###desloc
    def calcDesloc(self):
        self.interface_calculadora.chamar(
                var            = str(self.desloc),
                etiqueta       = 'desloc',
                funcao_retorno = self.calcDeslocRetorno,
                pegar_variavel = self.pegarDesloc,
                )


    def calcDeslocRetorno(self, valor):
        self.desloc = int(valor)
        self.painel.setVariavel('desloc', self.desloc)


    def pegarDesloc(self):
        return self.desloc

    ###desloc

    ###calc
    def calcFurosADiagonal(self):
        if self.furos  < 1: return
        if self.espaco < 1: return

        self.coordenadas = [
                (self.sistema.converterParaPassoX(x) + self.coord_x,
                 self.sistema.converterParaPassoY(y) + self.coord_y)
                for x, y in
                calcFurosADiagonal(self.furos, self.angulo, self.espaco, self.desloc)]
        
        self.pagina_total = 0
        self.pagina_total = len(self.coordenadas)

        self.setPaginacao()


