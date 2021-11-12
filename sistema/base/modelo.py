from base.conexao import Conexao
from config import *

class Modelo():
    
    def __init__(self, nome_tabela):
        self.__conexao = Conexao(MYSQL_HOST, MYSQL_USUARIO, MYSQL_SENHA, MYSQL_BANCO)
        self.__cursor  = self.__conexao.get_conexao().cursor()
        self.__nome_tabela = nome_tabela
    
    def __del__(self):
        self.__cursor.close()
    
    def obter_dados(self):
        instrucao = "SELECT * FROM {tabela}".format(tabela = self.__nome_tabela)
        try:
            self.__cursor.execute(instrucao)
            resultado = self.__cursor.fetchall()
            return resultado
        except:
            print ("Ocorreu um erro ao executar: ", self.__cursor._last_executed)
            return None
   
    def obter_por_id(self, id):
        instrucao = "SELECT * FROM {tabela} WHERE id=%s".format(tabela = self.__nome_tabela)
        self.__cursor.execute(instrucao, id)
        resultado = self.__cursor.fetch()
        return resultado

    def excluir_por_id(self, id):
        instrucao = "DELETE FROM {tabela} WHERE id=%s".format(tabela = self.__nome_tabela)
        self.__cursor.execute(instrucao, id)  

    def obter_cursor(self):
        return self.__cursor;
        
    def salvar(self):
        pass