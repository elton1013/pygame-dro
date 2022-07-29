import pygame
import json
import atexit
import os

from . import sensor

from .painel.trabalho          import Trabalho         as PainelTrabalho
from .painel.menu              import MenuTrabalho     as PainelMenuTrabalho
from .painel.menu              import MenuConfiguracao as PainelMenuConfiguracao
from .painel.caderno           import Caderno          as PainelCaderno
from .painel.calculadora       import Calculadora      as PainelCalculadora
from .painel.configuracao      import Configuracao     as PainelConfiguracao
from .painel.lista_referencias import ListaReferencias as PainelListaReferencias


from .interface.caderno      import Caderno      as InterfaceCaderno
from .interface.calculadora  import Calculadora  as InterfaceCalculadora
from .interface.configuracao import Configuracao as InterfaceConfiguracao
from .interface.referencias  import Referencias  as InterfaceReferencias



class App:
    def __init__(self):
        pygame.init()

        self.sensor = sensor.Sensor()
        self.loadVars()

        self.tamanho           = (640, 480)
        self.area_trabalho     = 'trabalho'
        self.ajuste_x          = 0
        self.ajuste_y          = 0
        self.correr            = True
        self.refe_selecionada  = None
        self.lista_referencias = []
        self.bandeiras         = 0
        self.bandeiras        |= pygame.NOFRAME
        #self.bandeiras        |= pygame.FULLSCREEN
        self.root              = pygame.display.set_mode(size = self.tamanho, flags = self.bandeiras)
        self.clock             = pygame.time.Clock()

        self.paineis = {
                'trabalho'      : PainelTrabalho(        root = self.root, tamanho = self.tamanho),
                'menu_trabalho' : PainelMenuTrabalho(    root = self.root, tamanho = self.tamanho),
                'menu_config'   : PainelMenuConfiguracao(root = self.root, tamanho = self.tamanho),
                'caderno'       : PainelCaderno(         root = self.root, tamanho = self.tamanho),
                'calculadora'   : PainelCalculadora(     root = self.root, tamanho = self.tamanho),
                'configuracao'  : PainelConfiguracao(    root = self.root, tamanho = self.tamanho),
                'referencias'   : PainelListaReferencias(root = self.root, tamanho = self.tamanho),
                }

        self.interfaces = {
                'trabalho'    : InterfaceCaderno(     **self.paineis, sistema = self, area_trabalho = 'trabalho'),
                'configurar'  : InterfaceConfiguracao(**self.paineis, sistema = self, area_trabalho = 'configurar'),
                'calculadora' : InterfaceCalculadora( **self.paineis, sistema = self, area_trabalho = 'calculadora'),
                'referencias' : InterfaceReferencias( **self.paineis, sistema = self, area_trabalho = 'referencias'),
                }

        self.interfaces['trabalho'].interface_calculadora    = self.interfaces['calculadora']
        self.interfaces['configurar'].interface_calculadora  = self.interfaces['calculadora']
        self.interfaces['referencias'].interface_calculadora = self.interfaces['calculadora']
        self.interfaces['referencias'].interface_trabalho    = self.interfaces['trabalho']

        if sensor.modelo == 'Fake':
            self.paineis['trabalho'].setEtiqueta('Fake')


    def loadVars(self):
        with open('config.txt') as f:
            d = json.loads(f.read())
            self.precisao_x = d['x']
            self.precisao_y = d['y']


    def saveVars(self):
        with open('config.txt', 'w') as f:
            d = {'x' : self.precisao_x,
                 'y' : self.precisao_y,}
            f.write(json.dumps(d))


    def setDesligar(self):
        atexit.register(self.desligar)


    def desligar(self):
        os.system('shutdown now')
        #print('desligando')


    def converterSinal(self): #converte a medida do sinal de passo para mm
        return ((self.sensor.leitura[0] - self.ajuste_x) * self.precisao_x,
                (self.sensor.leitura[1] - self.ajuste_y) * self.precisao_y)


    def converterParaPassoX(self, x): #converte medida de mm para passo
        return round(x / self.precisao_x)


    def converterParaPassoY(self, y): #converte medida de mm para passo
        return round(y / self.precisao_y)
        

    def loop(self):
        while self.correr:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.correr = False

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.interfaces.get(self.area_trabalho, self.interfaces['trabalho']).eventos(event)


            self.sensor.getLeitura()
            self.interfaces.get(self.area_trabalho, self.interfaces['trabalho']).rotina()
            self.interfaces.get(self.area_trabalho, self.interfaces['trabalho']).draw()
            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()


if __name__ == '__main__':
    app = App()
    app.loop()


