from django.urls import path, include
from app_cad_usuarios import views

urlpatterns = [
    #rota. view responsável, nome de referencia
    
    #usuarios.com
    path('cadastrar/',views.cadastro,name='cadastro'),

    path('/save', views.usuarios, name='save'),

    path('delete/<int:id>', views.delete, name='delete'),
    
    #usuarios.com/usuarios
    path('',views.home,name='listagem_usuarios'),

    #usuarios.com/editar
    path('editar/<int:id>', views.editar, name='editar'),

    path('update/<int:id>', views.update, name='update'),

    #usuarios.com/regras
    path('regras/',views.regras,name='regras'),

]