from base.modelo import Modelo

class Usuario(Modelo):
    Tabela = "usuarios"

    def __init__(self):
        super().__init__(self.Tabela);
        # Atributos da tabela 'usuarios'
        self.id = None;
        self.usuario = None;
        self.senha = None;
    
    def salvar(self):
        try:
            instrucao = "INSERT INTO {tabela} (usuario, senha) VALUES (%s, %s)".format(tabela = self.Tabela)
            self.obter_cursor().execute(instrucao, [self.usuario, self.senha])
            return True
        except:
            print ("Ocorreu um erro ao executar: ", self.obter_cursor()._last_executed)
            return False