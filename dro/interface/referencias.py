
import functools

from .trabalho import Trabalho
from .refe     import Refe, Modo


class Referencias(Trabalho):
    def __init__(self, referencias, **kwargs):
        super().__init__(**kwargs)

        self.referencias            = referencias
        self.paineis['referencias'] = referencias

        self.referencias.botoes['Origem'].comando     = functools.partial(self.addRef, 'Origem',     'XY')
        self.referencias.botoes['Referencia'].comando = functools.partial(self.addRef, 'Referencia', 'XY')
        self.referencias.botoes['Furo'].comando       = functools.partial(self.addRef, 'Furo',       'XY')
                                                                                       
        self.referencias.botoes['Centro'].comando     = functools.partial(self.addRef, 'Centro',     'XY')
        self.referencias.botoes['Centro X'].comando   = functools.partial(self.addRef, 'Centro X',   'X')
        self.referencias.botoes['Centro Y'].comando   = functools.partial(self.addRef, 'Centro Y',   'Y')
                                                                                       
        self.referencias.botoes['X'].comando          = functools.partial(self.addRef, 'X',          'X')
        self.referencias.botoes['Y'].comando          = functools.partial(self.addRef, 'Y',          'Y')
                                                                                      
        self.referencias.botoes['Borda X'].comando    = functools.partial(self.addRef, 'Borda X',    'X')
        self.referencias.botoes['Borda Y'].comando    = functools.partial(self.addRef, 'Borda Y',    'Y')
                                                                                       
        self.referencias.botoes['Mod Raio'].comando   = functools.partial(self.addRef, 'Mod Raio',   'XY')
        self.referencias.botoes['Mod Diagl'].comando  = functools.partial(self.addRef, 'Mod Diagl',  'XY')


    def addRef(self, etiqueta, tipo):
        self.sistema.area_trabalho = 'trabalho'

        nova_pos = 1
        for refe in self.sistema.lista_referencias:
            if refe.etiqueta != etiqueta:
                continue

            if refe.pos >= nova_pos:
                nova_pos = refe.pos + 1

        d = {
                'sistema'      : self.sistema,
                'etiqueta'       : etiqueta,
                'etiqueta_final' : f'{etiqueta} {nova_pos:02d}',
                'pos'            : nova_pos,
                'tipo'           : tipo,
                }

        if etiqueta.startswith('Mod'):
            self.sistema.lista_referencias.append(Modo(**d))

        else:
            self.sistema.lista_referencias.append(Refe(**d))

        self.interface_trabalho.configPaginacao()

