from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_vista, name='mi_vista'),
    path('mutations/', views.listar_mutations, name='listar_mutations'),
    path('diseases/', views.listar_diseases, name='listar_diseases'),
    path('crossing/', views.listar_crossing, name='listar_crossing'),
]
