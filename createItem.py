import cherrypy

from classes.tipo import *
from classes.produto import *

class CadastroProdutos():

    topo = open("html/cabecalho.html").read()
    fim = open("html/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()

    def montaFormulario(self,titulo="",tipo=0,valor=0,descricao=""):
        
        html = self.topo
        html += '''<form name="formCadastro" action="Cadastrar" method="post">
                       <p>
                           <label><b>Titulo do Produto:</b></label><br />
                           <input type="text" id="txtTitulo" name="txtTitulo" value="%s" size="50" maxlength="50" required /><br />
                           <label><b>Tipo do Produto:</b></label><br/>'''

        html += self.comboTipos()
        html += '''        
                           <br /><input type ="file" name = "img" id = "img" value = "%s"/><br />
                           <label><b>Preco do Produto:</b></label><br />
                           <input type = "text" value="%s" id = "valor" name = "valor" " required/>
                           <br /><label><b>Email:</b></label><br />
                           <input type = "email" placeholder = " exmplo@gmail.com" nome ="email" id ="email" value = "%s" />
                           <label><br /><b>Descricao:</b></label><br />
                           <textarea id="txtDescricao" name="txtDescricao" value = "%s" cols="50" rows="5" placeholder ="..."></textarea><br />
                           <input type="submit" id = "btnGravar" name = "btnGravar" value = "Gravar"/> 
                       </p>
                   </form> '''%(titulo,tipo,valor,descricao)

       # html += self.montaTabela()
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
    def Cadastrar(self,txtTitulo,txtTipo,img,valor,email,txtDescricao ,btnGravar ):
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
            return '''
                    <script>
                        alert("produto cadastrado")
                    </script>
            '''
    
    def montaTabela(self):
        html = '''<table class="alinha">
                    <tr>
                        <th>ID</th>
                        <th>id tipo</th>
                        <th>produto</th>
                        <th>valor</th>
                        <th>descricao</th>
                        <th>contato</th>
                    </tr>
        '''
        objTipo = Produtos()
        dados = objTipo.obterProdutos()
        for tp in dados:
            html += "<tr>" \
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td>%s</td>"\
                        "<td style='text-align:center'>[<a href='alterarProduto?id=%s'>Alterar</a>] " \
                            "[<a href='excluirProduto?id=%s'>Excluir</a>]" \
                    "</tr> \n" % (tp["id"], tp["tipo_id"], tp["titulo"], tp["valor"], tp["descricao"], tp["contato"])

        html += "</table><br/>"
        return html
    
    
    def alterarProduto(self,txtTitulo):
        pro = Produtos()
        dados = pro.set_titulo(txtTitulo)
        return self.montaFormulario(dados[0]["id"],dados[0]["tipo_id"],dados[0]["titulo"], dados[0]["valor"], dados[0]["descricao"], dados[0]["contato"])


    def excluirProduto(self,txtTitulo):
        pro = Produtos()
        dados = pro.procurarID(txtTitulo)
        dados = pro.excluir(dados)
