class Conta:
    def __init__(self, numero,titular,saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = float(saldo)

    
    def to_dict(self):
        return {
            'numero': self.numero,
            'titular': self.titular,
            'saldo': self.saldo
        }
    @classmethod
    def from_dict(cls, data):
        return cls(data['numero'], data['titular'], data['saldo'])
    
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
    FILE_PATH = 'data/contas.json'

    def __init__(self):
        self.contas = self._load()

    def _load(self):
        import json, os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            return [Conta.from_dict(item) for item in json.load(f)]

    def _save(self):
        import json
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.contas], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.contas

    def get_by_numero(self, numero):
        target_numero = str(numero)
        return next((c for c in self.contas if str(c.numero) == target_numero), None)

    def add(self, conta):
        self.contas.append(conta)
        self._save()

    def update(self, conta_atualizada):
        for i, c in enumerate(self.contas):
            if str(c.numero) == str(conta_atualizada.numero):
                self.contas[i] = conta_atualizada
                self._save()
                break

    def delete(self, conta_id):
        self.contas = [a for a in self.contas if a.id != conta_id]
        self._save()