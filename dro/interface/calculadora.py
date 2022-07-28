
import functools
from math import pi

from .interface import Interface


class Calculadora(Interface):
    def __init__(self, calculadora, **kwargs):
        super().__init__(**kwargs)

        self.calculadora = calculadora
        self.paineis['calculadora'] = calculadora
        self.var = '0'

        self.calculadora.botoes['Cancelar'].comando = self.cancelar
        self.calculadora.botoes['Limpar'].comando   = self.limpar
        self.calculadora.botoes['Back'].comando     = self.back
        self.calculadora.botoes['Get'].comando      = self.get
        self.calculadora.botoes['Set'].comando      = self.set
        self.calculadora.botoes['='].comando        = self.resolver

        self.calculadora.botoes['pi'].comando       = functools.partial(self.enterDigito, 'pi')
        self.calculadora.botoes['.'].comando        = functools.partial(self.enterDigito, '.')
        self.calculadora.botoes['('].comando        = functools.partial(self.enterDigito, '(')
        self.calculadora.botoes[')'].comando        = functools.partial(self.enterDigito, ')')
        self.calculadora.botoes['/'].comando        = functools.partial(self.enterDigito, '/')
        self.calculadora.botoes['*'].comando        = functools.partial(self.enterDigito, '*')
        self.calculadora.botoes['-'].comando        = functools.partial(self.enterDigito, '-')
        self.calculadora.botoes['+'].comando        = functools.partial(self.enterDigito, '+')

        self.calculadora.botoes['0'].comando        = functools.partial(self.enterDigito, '0')
        self.calculadora.botoes['1'].comando        = functools.partial(self.enterDigito, '1')
        self.calculadora.botoes['2'].comando        = functools.partial(self.enterDigito, '2')
        self.calculadora.botoes['3'].comando        = functools.partial(self.enterDigito, '3')
        self.calculadora.botoes['4'].comando        = functools.partial(self.enterDigito, '4')
        self.calculadora.botoes['5'].comando        = functools.partial(self.enterDigito, '5')
        self.calculadora.botoes['6'].comando        = functools.partial(self.enterDigito, '6')
        self.calculadora.botoes['7'].comando        = functools.partial(self.enterDigito, '7')
        self.calculadora.botoes['8'].comando        = functools.partial(self.enterDigito, '8')
        self.calculadora.botoes['9'].comando        = functools.partial(self.enterDigito, '9')


    def chamar(self, var, etiqueta, funcao_retorno, pegar_variavel):
        self.voltar_para    = self.sistema.area_trabalho
        self.var            = var               #str - valor inicial
        self.etiqueta       = etiqueta          #str - oq exibir no inicio da linha
        self.funcao_retorno = funcao_retorno    #def - como o valor final deve voltar/ou ser tratado
        self.pegar_variavel = pegar_variavel    #def - que retorna valor atual da variavel a ser alterada

        self.sistema.area_trabalho = 'calculadora'
        self.calculadora.setEtiqueta(self.etiqueta)
        self.calculadora.setDisplay(self.var)


    def cancelar(self):
        self.sistema.area_trabalho = self.voltar_para


    def limpar(self):
        self.var = ''
        self.calculadora.setDisplay(self.var)


    def back(self):
        try:
            self.var = self.var[:-1]
            self.calculadora.setDisplay(self.var)

        except:
            pass


    def get(self):
        self.var += str(self.pegar_variavel())
        self.calculadora.setDisplay(self.var)


    def set(self):
        try:
            var = float(self.var)
            self.funcao_retorno(var)

        except:
            pass

        self.sistema.area_trabalho = self.voltar_para


    def resolver(self):
        try:
            self.var = str(round(eval(self.var), 3))
            self.calculadora.setDisplay(self.var)
        except:
            pass


    def enterDigito(self, digito):
        self.var += digito
        self.calculadora.setDisplay(self.var)

