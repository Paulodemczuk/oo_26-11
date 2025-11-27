from bottle import request
from models.conta import ContaModel, Conta

class ContaService:
    def __init__(self):
        self.conta_model = ContaModel()

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
