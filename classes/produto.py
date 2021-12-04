from classes.banco import *

class Produtos():

    def __init__(self):

        self.__id = 0
        self.__id_tipo = 0
        self.__titulo = ''
        self.__valor = 0
        self.__descricao = ''
        self.__contato = ''
        self.__foto = ''
        self.__banco = Banco()


    def set_id_tipo(self,tipo):
        if str(tipo) != '':
            self.__id_tipo = tipo

    def set_titulo(self,titulo):
        if len(titulo) > 0:
            self.__titulo = titulo
    
    def set_valor(self,valor):
        if str(valor) != '':
            self.__valor = valor
    
    def set_descricao(self,desc):
        if len(desc) > 0:
            self.__descricao = desc
    
    def set_contato(self,contato):
        if len(contato) > 0:
            self.__contato = contato
    
    def set_foto(self,foto):
        if len(foto) > 0:
            self.__foto = foto
    
    def Gravar(self):

        sql = "insert into Anuncio (tipo_id,titulo,valor,descricao,contato,foto)"\
              "values('#id_tipo','#titulo','#valor','#descricao', '#contato', '#foto')"
        sql = sql.replace("#id_tipo",self.__id_tipo)
        sql = sql.replace("#titulo", self.__titulo)
        sql = sql.replace("#valor",self.__valor)
        sql = sql.replace("#descricao",self.__descricao)
        sql = sql.replace("#contato",self.__contato)
        sql = sql.replace("#foto",self.__foto)
        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):

        sql = "delete from Anuncio where id = #id"
        sql = sql.replace('#id',str(self.__id))
        return self.__banco.executarSelect(sql)

    def obterProdutos(self):
        sql = "select tipo_id,titulo,valor,descricao,contato from Anuncio order by name "
        return self.__banco.executarSelect(sql)