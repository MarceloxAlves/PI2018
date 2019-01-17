from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *;
from .models import Account


@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        account_serializer = AccountSerializer(accounts, many=True)
        return Response(status=status.HTTP_200_OK, data=account_serializer.data)

    if request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.is_valid():
            account_serializer.save();
            return Response(status=status.HTTP_201_CREATED, data=account_serializer.data)
    return Response(data={"erros": account_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
def account_detail(request, id):
    erros = {}
    try:
        account = Account.objects.get(id=id)
    except Account.DoesNotExist:
        erros["conta"] = "Esta conta não existe"
        return Response(data={"erros": [erros]}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"account": serializer.data, "msg": "Account alterada com sucesso!"})
        return Response(data={"erros": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response(data={"msg": "Conta deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["PATCH"])
def credit(request, id):
    erros = {}
    try:
        account = Account.objects.get(id=id)
    except Account.DoesNotExist:
        erros["conta"] = "Esta conta não existe"
        return Response(data={"erros": [erros]}, status=status.HTTP_404_NOT_FOUND)
    request.data["balance"] = request.data["value"]
    serializer = AccountSerializer(account, data=request.data, partial=True)
    if serializer.is_valid():
        instance = serializer.instance
        instance.depositar(serializer.validated_data["balance"])
        instance.save()
        msg = "Depósito realizado com sucesso!"
        return Response(data={"account": serializer.data, "msg": msg})
    return Response(data={"erros": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def debit(request, id):
    erros = {}
    try:
        account = Account.objects.get(id=id)
    except Account.DoesNotExist:
        erros["conta"] = "Esta conta não existe"
        return Response(data={"erros": [erros]}, status=status.HTTP_404_NOT_FOUND)
    request.data["balance"] = request.data["value"]
    serializer = AccountSerializer(account, data=request.data, partial=True)
    if serializer.is_valid():
        instance = serializer.instance
        try:
            instance.sacar(serializer.validated_data["balance"])
        except Account.BalanceException as ex:
            erros["conta"] = str(ex)
            return Response(data={"erros": [erros]}, status=status.HTTP_400_BAD_REQUEST)
        msg = "Saque realizado com sucesso!"
        instance.save()
        serializer = AccountSerializer(instance)
        return Response(data={"account": serializer.data, "msg": msg})
    return Response(data={"erros": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
