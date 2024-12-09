from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Historia, Comment
from django.shortcuts import render, get_object_or_404


"""Primeira parte de implementação da views arquivos funcionais sem forms"""
"""def list_historias(request):
    historias_list = Historia.objects.all()
    context = {'historias_list': historias_list}
    return render(request, 'historias/index.html', context)"""

"""
def detail_historia(request, historia_id):
    historia = Historia.objects.get(pk=historia_id)
    context = {'historia': historia}
    return render(request, 'historias/detail.html', context)

def detail_historia(request, historia_id):
    historia = get_object_or_404(Historia, pk=historia_id)
    context = {'historia': historia}
    return render(request, 'historias/detail.html', context)
"""

def search_historias(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        historias_list = Historia.objects.filter(name__icontains=search_term)
        context = {"historias_list": historias_list}
    return render(request, 'historias/search.html', context)

"""
def update_historia(request, historia_id):
    historia = get_object_or_404(Historia, pk=historia_id)

    if request.method == 'POST':
        historia.name = request.POST['name']
        historia.data = request.POST['data']
        historia.capa = request.POST['capa']
        historia.relato = request.POST['relato']
        historia.save()
        return HttpResponseRedirect(
            reverse('historias:detail', args=(historia.id, )))

    context = {'historia': historia}
    return render(request, 'historias/update.html', context)
"""
"""
def delete_historia(request, historia_id):
    historia = get_object_or_404(Historia, pk=historia_id)

    if request.method == "POST":
        historia.delete()
        return HttpResponseRedirect(reverse('historias:index'))

    context = {'historia': historia}
    return render(request, 'historias/delete.html', context)
"""
"""Segunda parte de implementação da views arquivos funcionais com um forms"""
from .forms import HistoriaForm, CommentForm

"""
def create_historia(request):
    if request.method == 'POST':
        historia_name = request.POST['name']
        historia_data = request.POST['data']
        historia_capa = request.POST['capa']
        historia_relato = request.POST['relato']
        historia = Historia(name=historia_name,
                      data=historia_data,
                      capa=historia_capa,
                      relato=historia_relato)
        historia.save()
        return HttpResponseRedirect(
            reverse('historias:detail', args=(historia.id, )))
    else:
        form = HistoriaForm()
        context = {'form': form}
        return render(request, 'historias/create.html', context)
"""


"""Terceira parte com views genéricas"""
from django.views import generic
from django.urls import reverse_lazy

class HistoriaListView(generic.ListView):
    model = Historia
    template_name = 'historias/index.html'

class HistoriaDetailView(generic.DetailView):
    model = Historia
    template_name = 'historias/detail.html'

class HistoriaCreateView(generic.CreateView):
    model = Historia
    form_class = HistoriaForm
    template_name = 'historias/create.html'
    success_url = reverse_lazy('historias:index')

class HistoriaUpdateView(generic.UpdateView):
    model = Historia
    fields = ['name', 'capa', 'relato']
    template_name = 'historias/update.html'
    success_url = reverse_lazy('historias:index')

class HistoriaDeleteView(generic.DeleteView):
    model = Historia
    template_name = 'historias/delete.html'
    success_url = reverse_lazy('historias:index')

# Implementação dos comentarios nos posts
def create_comment(request, historia_id):
    historia = get_object_or_404(Historia, pk=historia_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            review_autor = form.cleaned_data['autor']
            review_texto = form.cleaned_data['texto']
            review = Comment(autor=review_autor,
                            texto=review_texto,
                            historia=historia)
            review.save()
            return HttpResponseRedirect(
                reverse('historias:detail', args=(historia_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'historia': historia}
    return render(request, 'historias/comment.html', context)

# Implementação das categorias nos posts
from .models import Category

class CategoriaListView(generic.ListView):
    model = Category
    template_name = 'historias/categorias.html'


class CategoriaCreateView(generic.CreateView):
    model = Category
    template_name = 'historias/createcategoria.html'
    fields = ['nome']
    success_url = reverse_lazy('historias:categorias')


def historiascatego(request, pk):
    historias_catego = Historia.objects.filter(categoria=pk)
    return render(request, 'historias/indexcatego.html', {'historiascatego': historias_catego})