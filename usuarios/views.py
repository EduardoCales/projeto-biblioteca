from django.shortcuts import render

def cadastro_view(request):
    return render(request, 'usuarios/pages/cadastro_view.html')