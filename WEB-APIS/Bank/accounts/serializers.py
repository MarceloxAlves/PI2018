from rest_framework import serializers
from .models import Account
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'owner', 'balance', 'creation_date']

    def validate_balance(self, value):
        if value == 0:
            raise serializers.ValidationError("valor não pode ser zero");
        if value < 0:
            raise serializers.ValidationError("Não é possível valor negativo");
        return value

    def validate_creation_date(self, value):
        if value:
            raise serializers.ValidationError("Data inválida")
        return value

