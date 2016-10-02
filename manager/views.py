from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ScriptlistModel
from .forms import ScriptlistForm

# -------------------------------------------------------------
def index(request):
    template_name = 'manager/index.html'

    if request.method == 'POST':
        forms = ScriptlistForm(request.POST, request.FILES)
        if forms.is_valid():
            newpost = ScriptlistModel(
                author=forms.cleaned_data['author'],
                tcid=forms.cleaned_data['tcid'],
                detail=forms.cleaned_data['detail'],
                scrfile=request.FILES['scrfile'],
            )
            newpost.save()
            return HttpResponseRedirect(reverse('manager:index'))
    else:
        forms = ScriptlistForm()
    scripts = ScriptlistModel.objects.order_by('-now')#[0:5]
    totalCnt = ScriptlistModel.objects.all().count()

    return render(request, template_name, {
                                        'scripts':scripts,
                                        'forms':forms,
                                        'totalCnt':totalCnt
    })

# -------------------------------------------------------------

def detail(request, id):
    template_name = 'manager/view.html'

    form = ScriptlistForm()

    scripts = ScriptlistModel.objects.get(id=id)
    return render(request, template_name, {
                                        'scripts':scripts,
                                        'form':form
    })

# -------------------------------------------------------------

def delete(request, id):

    posts = ScriptlistModel.objects.get(id=id)
    if request.method == 'POST':
        posts.delete()
        return redirect('manager:detail', id)
    return render(request, 'manager/view.html', {'posts':posts} )

# -------------------------------------------------------------

def del_confirm(request, id):

    scripts =ScriptlistModel.objects.get(id=id)
    return render(request, 'manager/del.html', {'scripts':scripts})

# -------------------------------------------------------------

def modify(request, id):

    posts =ScriptlistModel.objects.get(id=id)
    if request.method == 'POST':
        form = ScriptlistForm(request.POST, instance=posts)
        if form.is_valid():
            modpost = posts(
                author=forms.cleaned_data['author'],
                tcid=forms.cleaned_data['tcid'],
                detail=forms.cleaned_data['detail'],
                scrfile=request.FILES['scrfile']
            )
            modpost.save()
            return HttpResponseRedirect(reverse('manager:index'))
    else:
        form = ScriptlistForm(initial={'author':posts.author, 'tcid':posts.tcid, 'scrfile':posts.scrfile, 'detail':posts.detail, 'now':posts.now})

    return render(request, 'manager/modify.html', {'form':form, 'posts':posts})