from bottle import Bottle, request, response
from .base_controller import BaseController
from services.conta_service import ContaService

class ContaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.conta_service = ContaService()
        self.setup_routes()

    def setup_routes(self):
        
        self.app.route('/conta', method='GET', callback=self.index)
        self.app.route('/conta/criar',method=['GET', 'POST'], callback=self.criar)
        self.app.route('/conta/saldo/<numero>', method='GET', callback=self.ver_saldo)
        self.app.route('/conta/depositar/<numero>', method=['GET', 'POST'], callback=self.depositar)
        self.app.route('/conta/sacar/<numero>', method=['GET', 'POST'], callback=self.sacar)

    def index(self):
        
        contas = self.conta_service.listar_todas()
        return self.render('contas', contas=contas)

    def criar(self):
        if request.method == 'GET':
            return self.render('conta_form', action='/conta/criar')
        
        sucesso, mensagem = self.conta_service.criar_conta()
        if sucesso:
            self.redirect('/conta')
        else:
            return f"Erro: {mensagem}"

    def ver_saldo(self, numero):
        saldo = self.conta_service.consultar_saldo(numero)
        if saldo is not None:
            return f"O saldo da conta {numero} é R$ {saldo:.2f}"
        return "Conta não encontrada"
    
    def depositar(self, numero):
        if request.method == 'GET':
            return self.render('operacao', numero=numero, tipo='depositar')
        
        valor = request.forms.get('valor')
        sucesso, msg = self.conta_service.depositar(numero, valor)
        
        if sucesso:
            self.redirect('/conta')
        else:
            return f"Erro: {msg} <br><a href='/conta'>Voltar</a>"

    def sacar(self, numero):
        if request.method == 'GET':
            return self.render('operacao', numero=numero, tipo='sacar')
        
        valor = request.forms.get('valor')
        sucesso, msg = self.conta_service.sacar(numero, valor)
        
        if sucesso:
            self.redirect('/conta')
        else:
            return f"Erro: {msg} <br><a href='/conta'>Voltar</a>"


conta_routes = Bottle()
conta_controller = ContaController(conta_routes)