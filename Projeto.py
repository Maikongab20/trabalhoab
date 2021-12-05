import cherrypy
import os
# eu fiz o cadastro de produtos mas nao consegui fazer a tabela e excluir nao esta terminado nao sei o que estou fazendo de errado o site foi eu que terminei. maikon e andre
from pageTipo import PaginaTipo
#from pageEquipe import PaginaEquipe
from createItem import CadastroProdutos

local_dir = os.path.dirname(__file__)

class Principal():
    topo = open("html/cabecalho.html").read()
    rodape = open("html/rodape.html").read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        #html += self.montaAnuncios()

        html +=  self.rodape

        return html

 #   def obter(self):
 #        sql = "select id, titulo, valor, foto " \
 #              "from Anuncio " \
 #              "order by titulo"
 #        dados = self.__banco.executarSelect(sql)
 #        return dados

 #   def montaAnuncios(self):
 #        objAnuncio = Anuncio()
 #        dados = objAnuncio.obter()
 #        if len(dados) > 0:
 #            html = ""
 #            for a in dados:
 #                html += "<div style='width:320px; display:inline-block; padding: 5px; text-align:center'>" \
 #                            "<img src='%s?random=%s' alt='%s' /><br/>%s<br/>R$ %.2f" \
 #                        "</div> \n" % (a["foto"], a["id"], a["titulo"], a["titulo"], a["valor"])
 #        else:
 #            html = "<p>Não há anúncios a sere exmibidos..."
 #        return html


local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}


root = Principal() 
root.pgTipo = PaginaTipo() 
root.createItem = CadastroProdutos()
#root.pgEquipe = PaginaEquipe() 

cherrypy.quickstart(root,config=local_config)
