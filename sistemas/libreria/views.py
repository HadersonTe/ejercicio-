from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import libro, Categoria
from .forms import LibroForm, CategoriaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

@login_required
def libros(request):
    libros = libro.objects.all()
    return render(request, "libros/index.html", {"libros": libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, "libros/crear.html", {"formulario": formulario})

def editar(request, id):
    libro_ed = libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro_ed)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, "libros/editar.html", {"formulario": formulario})

def eliminar(request, id):
    libroe = libro.objects.get(id=id)
    libroe.delete()
    return redirect('libros')

@login_required
def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/index.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    formulario = CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categorias')
    return render(request, 'categorias/crear.html', {'formulario': formulario})

@login_required
def editar_categoria(request, id):
    cate_ed = Categoria.objects.get(id=id)
    formulario = CategoriaForm(request.POST or None, request.FILES or None, instance=cate_ed)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('categorias')
    return render(request, 'categorias/editar.html', {'formulario': formulario})

@login_required
def eliminar_categoria(request, id):
    cate_ed = Categoria.objects.get(id=id)
    cate_ed.delete()
    return redirect('categorias')