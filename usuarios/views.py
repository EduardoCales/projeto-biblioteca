from django.http import Http404
from django.shortcuts import redirect, render

from usuarios.forms import RegisterForm


def cadastro_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'usuarios/pages/cadastro_view.html', context={
        'form': form,
    })


def cadastro_create(request):
    if not request.POST:
        raise Http404()
    
    POST= request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    return redirect('usuarios:cadastro')