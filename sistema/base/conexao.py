import pymysql

class Conexao:

    def __init__(self, host, user, password, database):
        self.__conexao = None
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.conectar()
    
    def __del__(self):
        if self.__conexao:
            self.__conexao.close()

    def conectar(self):
        try:
            self.__conexao = pymysql.connect(host=self.__host,
                                             user=self.__user,
                                             password=self.__password,
                                             database=self.__database,
                                             autocommit=True)
            return True
        except:
            print("Falha ao conectar!")
            return False
    
    def get_conexao(self):
        return self.__conexao
