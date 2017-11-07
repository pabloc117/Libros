from django.shortcuts import render
from .models import Libros
from .models import Usuario
from .models import Prestamo
from .forms import LibrosForm
from .forms import UsuarioForm
from .forms import PrestamoForm
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def nuevo(request):
    form = LibrosForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)

@login_required
def nuevoU(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)

@login_required
def prestamo(request):
    form = PrestamoForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    else:
        form2 = LibrosForm()

    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)


@login_required
def lista(request):
    queryset = Libros.objects.all().order_by("-created_date")
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
        }
    else:
        context = {
            "title": "Inicie sesion para ver la lista de articulos"
        }
    return render(request,"index.html",context)
