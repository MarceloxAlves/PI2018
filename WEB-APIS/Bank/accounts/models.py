from django.db import models
from datetime import datetime

# Create your models here.
class Account(models.Model):
    owner = models.CharField(max_length=100)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    creation_date = models.DateTimeField(default=datetime.now)


    def sacar(self, valor):
        if valor < 0:
            raise self.BalanceException("Não é possivel valor negativo")
        elif self.balance >= valor:
            self.balance -= valor
        else:
            raise self.BalanceException("Saldo insuficiente")

    def depositar(self, valor):
        self.balance += valor


    #Exception
    class BalanceException(Exception):
        pass


