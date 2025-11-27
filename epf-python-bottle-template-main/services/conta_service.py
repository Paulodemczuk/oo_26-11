from bottle import request
from models.conta import ContaModel, Conta

class ContaService:
    def __init__(self):
        self.conta_model = ContaModel()
    
    def criar_conta(self):
        numero = request.forms.get('numero')
        titular = request.forms.get('titular')
        saldo = request.forms.get('saldo', 0.0)
        
        if not numero or not titular:
            return False, "Número e Titular são obrigatórios"

        nova_conta = Conta(numero, titular, saldo)
        self.conta_model.add(nova_conta)
        return True, "Conta criada com sucesso"
    
    def consultar_saldo(self, numero):
        conta = self.conta_model.get_by_numero(numero)
        if conta:
            return conta.saldo
        return None
    
    def listar_todas(self):
        return self.conta_model.get_all()

    def get_all(self):
        return self.conta_model.get_all()

    def save(self):
        last_id = max([a.id for a in self.conta_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        description = request.forms.get('description')
        done = request.forms.get('done') == 'on'
        conta = Conta(new_id, name, description, done)
        self.conta_model.add(conta)

    def get_by_id(self, conta_id):
        return self.conta_model.get_by_id(conta_id)

    def edit(self, conta):
        conta.name = request.forms.get('name')
        conta.description = request.forms.get('description')
        conta.done = request.forms.get('done') == 'on'
        self.conta_model.update(conta)

    def delete(self, conta_id):
        self.conta_model.delete(conta_id)
        
    def depositar(self, numero, valor):
        conta = self.conta_model.get_by_numero(numero)
        if not conta:
            return False, "Conta não encontrada"

        try:
            valor_float = float(valor)
        except ValueError:
            return False, "Valor inválido"

        if conta.depositar(valor_float):
            self.conta_model.update(conta)
            return True, "Depósito realizado com sucesso"
        return False, "Valor de depósito deve ser positivo"

    def sacar(self, numero, valor):
        conta = self.conta_model.get_by_numero(numero)
        if not conta:
            return False, "Conta não encontrada"

        try:
            valor_float = float(valor)
        except ValueError:
            return False, "Valor inválido"

        if conta.sacar(valor_float):
            self.conta_model.update(conta)
            return True, "Saque realizado com sucesso"
        return False, "Saldo insuficiente ou valor inválido"
