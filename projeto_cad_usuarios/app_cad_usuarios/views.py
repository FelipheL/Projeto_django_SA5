from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario


def home(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def cadastro(request):
    return render(request, 'usuarios/home.html')

def delete(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect(home)

def update(request, id):
    usuarioNovo = Usuario.objects.get(id_usuario=id)
    
    novo_nome = request.POST.get('nome')
    nova_idade = request.POST.get('idade')
    
    usuarioNovo.nome = novo_nome
    usuarioNovo.idade = nova_idade
    usuarioNovo.save()
    return redirect(home)

def usuarios(request):
    #Salvar os dados da tela apra o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.id = request.POST.get('id_usuario')
    novo_usuario.save()
    #Exibir todos os usuários já cadastrados em uma nova pagina.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html',usuarios)

def editar(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    return render(request, "usuarios/editar.html", {"usuario":usuario})



def regras(request):
    return render(request, 'usuarios/regras.html')

def search(request):
    return render(request, 'usuarios/search.html')