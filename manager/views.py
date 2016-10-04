from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Document
from .forms import ScriptlistForm

# -------------------------------------------------------------
def index(request):
    template_name = 'manager/index.html'

    if request.method == 'POST':
        forms = ScriptlistForm(request.POST, request.FILES)
        if forms.is_valid():
            newpost = Document(
                author=forms.cleaned_data['author'],
                tcid=forms.cleaned_data['tcid'],
                detail=forms.cleaned_data['detail'],
                docfile=request.FILES['docfile'],
            )
            newpost.save()
            return HttpResponseRedirect(reverse('manager:index'))
    else:
        forms = ScriptlistForm()
    scripts = Document.objects.order_by('-now')#[0:5]
    totalCnt = Document.objects.all().count()

    return render(request, template_name, {
                                        'scripts':scripts,
                                        'forms':forms,
                                        'totalCnt':totalCnt
    })

# -------------------------------------------------------------

def detail(request, id):
    template_name = 'manager/view.html'

    form = ScriptlistForm()

    scripts = Document.objects.get(id=id)
    return render(request, template_name, {
                                        'scripts':scripts,
                                        'form':form
    })

# -------------------------------------------------------------

def delete(request, id):

    posts = Document.objects.get(id=id)

    return render(request, 'manager/del.html', {'posts':posts} )

# -------------------------------------------------------------

def del_confirm(request, id):
    try:
        scripts = Document.objects.get(id=id)
        scripts.delete()
    except:
        raise Http404('Do not delete!')
    return HttpResponseRedirect(reverse('manager:index'))

# -------------------------------------------------------------

def modify(request, id):

    posts = Document.objects.get(id=id)

    print (request)
    if request.method == 'POST':
        form = ScriptlistForm(request.POST, request.FILES)

        if form.is_valid():
            modpost = posts(
                author=form.cleaned_data['author'],
                tcid=form.cleaned_data['tcid'],
                detail=form.cleaned_data['detail'],
                docfile=request.FILES['docfile']
            )
            modpost.save()
            return HttpResponseRedirect('/manager/detail/')

    else:

        form = ScriptlistForm(
            initial={
                'author':posts.author,
                'tcid':posts.tcid,
                'docfile':posts.docfile,
                'detail':posts.detail,
                'now':posts.now}
        )
    return render(request, 'manager/modify.html', {'form':form, 'posts':posts})
