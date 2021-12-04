import cherrypy

from classes.tipo import *
from classes.produto import *

class CadastroProdutos():

    topo = open("html/cabecalho.html").read()
    fim = open("html/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()

    def montaFormulario(self):
        
        html = self.topo
        html += '''<form name="formCadastro" action="Cadastrar" method="post">
                       <p>
                           <label><b>Titulo do Produto:</b></label><br />
                           <input type="text" id="txtTitulo" name="txtTitulo" value="" size="50" maxlength="50" required /><br />
                           <label><b>Tipo do Produto:</b></label><br/>'''

        html += self.comboTipos()
        html += '''        
                           <br /><input type ="file" name = "img" id = "img" value = ""/><br />
                           <label><b>Preco do Produto:</b></label><br />
                           <input type = "text" value="" id = "valor" name = "valor" " required/>
                           <br /><label><b>Email:</b></label><br />
                           <input type = "email" placeholder = " exmplo@gmail.com" nome ="email" id ="email" value = "exemplo@gmail.com" />
                           <label><br /><b>Descricao:</b></label><br />
                           <textarea id="txtDescricao" name="txtDescricao" cols="50" rows="5" placeholder ="..."></textarea><br />
                           <input type="submit" id = "btnGravar" name = "btnGravar" value = "Gravar"/> 
                       </p>
                   </form> '''

        html += self.montarTabela()
        return html

    def comboTipos(self):
        objTipo = Tipo()
        dados = objTipo.obterTipos()
        html = "<select id='txtTipo' name='txtTipo'>"
        for tp in dados:
            html += "<option value='%s'>%s</option>\n" % (tp["id"], tp["nome"])
        html += "</select>"
        return html
    
    @cherrypy.expose()
    def Cadastrar(self,txtTitulo,txtTipo,img,valor,email = '',txtDescricao = '',btnGravar = ''):
        if len(txtTitulo) > 0:
            pro = Produtos()
            pro.set_titulo(txtTitulo)
            pro.set_id_tipo(txtTipo)
            pro.set_foto(img)
            pro.set_valor(valor)
            pro.set_contato(email)
            pro.set_descricao(txtDescricao)
            pro.Gravar()
            raise cherrypy.HTTPRedirect("/createItem")

    def montarTabela(self):

        html = '''
                <tabela = "alinha">
                <tr>
                    <th>id</th>
                    <th>id_tipo</th>
                    <th>titulo</th>
                    <th>valor</th>
                    <th>descricao</th>
                    <th>contato</th>
                </tr>
        
        '''
        pro = Produtos()
        dados = pro.obterProdutos()
        for tp in dados:
            html += "<tr>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td style='text-align:center'>[<a href='alterarAnuncio?id=%s'>Alterar</a>] " \
                            "[<a href='excluirProduto?idAnuncio=%s'>Excluir</a>]" \
                    "</tr> \n" % (tp["id"], tp["id_tipo"], tp["titulo"], tp["valor"], tp["descricao"], tp["contato"])

            html += "</tabela><br />"