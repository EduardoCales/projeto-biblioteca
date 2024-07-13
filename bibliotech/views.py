from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from bibliotech.models import Livro

def home(request):
    livros = Livro.objects.all().order_by('-id')
    return render(request, 'bibliotech/pages/home.html', context={
        'livros': livros,
    })

def category(request, category_id):
    livros = get_list_or_404 (
        Livro.objects.filter(
            category__id=category_id
        ).order_by('-id')
    )

    return render(request, 'bibliotech/pages/category.html', context= {
        'livros': livros,
        'title': f'{livros[0].category.name}'
    })

def livro(request, id):
    livro = get_object_or_404(Livro, pk=id)

    return render(request, 'bibliotech/pages/livro-view.html', context={
        'livro': livro,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404

    return render(request, 'bibliotech/pages/search.html', context={
        'page_title': f'Search for "{search_term}" |'
    })