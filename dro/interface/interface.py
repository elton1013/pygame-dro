
class Interface:
    def __init__(self, sistema, area_trabalho, **kwargs):
        self.sistema       = sistema
        self.paineis       = {}
        self.area_trabalho = area_trabalho


    def eventos(self, evento):
        for painel in self.paineis.values():
            for botao in painel.botoes.values():
                if botao.click(evento):
                    return


    def rotina(self): pass


    def draw(self):
        for painel in self.paineis.values():
            painel.draw()

