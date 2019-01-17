from django.urls import path, include
from .views import *

urlpatterns = [
    path('', account_list),
    path('<int:id>', account_detail),
    path('<int:id>/credit', credit),
    path('<int:id>/debit', debit),
]
