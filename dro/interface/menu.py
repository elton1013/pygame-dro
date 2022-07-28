
from .interface import Interface


##menu de cabeçalho
class MenuTrabalho(Interface):
    def __init__(self, menu_trabalho, **kwargs):
        super().__init__(**kwargs)

        self.menu = menu_trabalho
        self.paineis['menu'] = menu_trabalho

        self.menu.botoes['Configurar'].comando = self.configurar
        self.menu.botoes['Fechar'].comando     = self.fechar
        self.menu.botoes['Desligar'].comando   = self.desligar

    
    def configurar(self):
        self.sistema.area_trabalho = 'configurar'
    

    def fechar(self):
        self.sistema.correr = False


    def desligar(self):
        self.sistema.setDesligar()
        self.fechar()


##menu de cabeçalho
class MenuConfig(Interface):
    def __init__(self, menu_config, **kwargs):
        super().__init__(**kwargs)

        self.menu = menu_config
        self.paineis['menu'] = menu_config

        self.menu.botoes['Voltar'].comando = self.voltar
        self.menu.botoes['Salvar'].comando = self.salvar


    def voltar(self):
        self.sistema.area_trabalho = 'trabalho'


    def salvar(self):
        self.sistema.saveVars()
        self.sistema.area_trabalho = 'trabalho'

