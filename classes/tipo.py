from classes.banco import *

class Tipo():
    ''' Documentação da classe
    - Aqui devemos descrever os objetivos da classe e suas funcionalidades
    - Toda classe é composta por propriedades e métodos
    '''

    def __init__(self):
        # atributos públicos

        # atributos privados
        self.__id = 0
        self.__nome = ''
        self.__banco = Banco() #É o objeto que materializa todas as ações e propriedades declaradas na classe Banco

    # métodos
    def set_id(self, pId):#setar o valor
        if pId > 0: #Validação dos valores a serem associados a propriedade
            self.__id = pId

    def set_nome(self, pNome):
        if len(pNome) > 0: #Validação dos valores a serem associados a propriedade
            self.__nome = pNome

    def get_id(self):#obter valor
        return self.__id

    def get_nome(self):
        return self.__nome

    def gravar(self):
        #sql = "insert into Tipo (nome,cor) " \
        #      "values ('#nome','#cor')"
        # insert into Tipo (nome,cor) values ('TIPO NOVO','AZUL')
        sql = "insert into Tipo (nome) " \
              "values ('#nome')"
        # insert into Tipo (nome) values ('TIPO NOVO')
        sql = sql.replace("#nome", self.__nome) #substitue trechos da string
        #sql = sql.replace("#cor", self.__nome)
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        sql = "update Tipo set nome = '#nome' " \
              "where id = #id"
        sql = sql.replace('#nome', self.__nome)
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):
        sql = "delete from Tipo where id = #id"
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)

    # devolve um tipo em específico
    def obterTipo(self, id = 0):
        if id != 0:
            self.__id = id
        sql = "select id, nome from Tipo where id = #id"
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    # devolve todos os tipos
    def obterTipos(self):
        sql = "select id, nome from Tipo order by nome"
        return self.__banco.executarSelect(sql)