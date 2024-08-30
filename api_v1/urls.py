from django.urls import path

from api_v1.views import add, subtract, multiply, divide

app_name = 'api'

urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide')
]
