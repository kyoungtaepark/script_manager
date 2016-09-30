from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ScriptlistModel
from .forms import ScriptlistForm

def index(request):
    template_name = 'manager/index.html'

    if request.method == 'POST':
        forms = ScriptlistForm(request.POST, request.FILES)
        if forms.is_valid():
            newpost = ScriptlistModel(
                author=forms.cleaned_data['author'],
                tcid=forms.cleaned_data['tcid'],
                detail=forms.cleaned_data['detail'],
                scrfile=request.FILES['scrfile']
            )
            newpost.save()
            return HttpResponseRedirect(reverse('manager:index'))
    else:
        forms = ScriptlistForm()
    scripts = ScriptlistModel.objects.order_by('-now')
    totalCnt = ScriptlistModel.objects.all().count()

    return render(request, template_name, {'scripts':scripts, 'forms' : forms, 'totalCnt': totalCnt})

def detail(request, id):
    template_name = 'manager/view.html'

    form = ScriptlistForm()

    scripts = ScriptlistModel.objects.get(id=id)
    return render(request, template_name, {'scripts':scripts, 'form':form })

def modify(request, id):

    return render(request, 'manager/modify.html')

def delete(request, id):

    posts = ScriptlistModel.objects.get(id=id)
    if request.method == 'POST':
        posts.delete()
        return redirect('manager:detail', id)
    return render(request, 'manager/view.html', {'posts':posts})

def confirm(request, id):

    posts =ScriptlistModel.objects.get(id=id)
    return render(request, 'manager/confirm.html')