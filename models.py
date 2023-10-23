from forms import *


class Botao():
    def __init__(self):
        self.form = Form_rodada()
        self.min = 1
        self.max = 38
        self.campo = self.form.rodada.data

