class Conta:
    def __init__(self, numero,titular,saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __init__(self, numero,titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0
    
    def to_dict(self):
        return {
            'numero': self.numero,
            'titular': self.titular,
            'saldo': self.saldo
        }
    
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
    
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

class ContaModel:
    FILE_PATH = 'data/activities.json'

    def __init__(self):
        self.activities = self._load()

    def _load(self):
        import json, os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            return [Conta.from_dict(item) for item in json.load(f)]

    def _save(self):
        import json
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.activities], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.activities

    def get_by_id(self, conta_id):
        return next((a for a in self.activities if a.id == conta_id), None)

    def add(self, conta):
        self.activities.append(conta)
        self._save()

    def update(self, updated_conta):
        for i, a in enumerate(self.activities):
            if a.id == updated_conta.id:
                self.activities[i] = updated_conta
                self._save()
                break

    def delete(self, conta_id):
        self.activities = [a for a in self.activities if a.id != conta_id]
        self._save()