from django.shortcuts import render, redirect, get_object_or_404
from .forms import InfForm
from .models import Information
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


def index(request):
    all_inf = Information.objects.all()
    return render(request, 'index.html', {'all_inf' : all_inf})

def my_index(request):
    my_inf = Information.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_inf' : my_inf})

@login_required(login_url='/login/')
def create(request):
    if request.method == "POST":
        filled_form = InfForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('index')
    inf_form = InfForm()
    return render(request, 'create.html', {'inf_form' : inf_form})

@login_required(login_url='/login/')
def detail(request, inf_id):
    my_inf = get_object_or_404(Information, pk=inf_id)
    return render(request, 'detail.html', {'my_inf' : my_inf})

def delete(request, inf_id):
    my_inf = Information.objects.get(pk=inf_id)
    if request.user == my.inf.author:
        my_inf.delete()
        return redirect('index')
    
    raise PermissionDenied

def update(request, inf_id):
    my_inf = Information.objects.get(pk=inf_id)
    inf_form = InfForm(instance=my_inf)
    if request.method == "POST":
        updated_form = InfForm(request.POST, instance=my_inf)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html', {'inf_form' : inf_form})