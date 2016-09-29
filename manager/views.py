from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ScriptlistModel, CommentModel
from .forms import ScriptlistForm, CommentForm

def index(request):

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

    return render(request, 'manager/index.html',{'scripts':scripts, 'forms' : forms})



def detail(request, id):

    scripts = ScriptlistModel.objects.get(id=id)

    if request.method == 'POST':
        commentform = CommentForm(request.POST)

        if commentform.is_valid():
            newcomment = CommentModel(
                script=ScriptlistModel.objects.get(id=id),
                writer=commentform.cleaned_data['writer'],
                comments=commentform.cleaned_data['comments']
            )
            newcomment.save()
            return
    else:

        commentform = CommentForm()

    comments = CommentModel.objects.order_by('-time')

    return render(request, 'manager/view.html', {'scripts':scripts,'commentform':commentform, 'comments': comments})


def modify(request, id):

    return render(request, 'manager/modify.html', {'id': id})

def delete(request, id):

    posts = ScriptlistModel.objects.get(id=id)
    if request.method == 'POST':
        posts.delete()
        return redirect('manager:detail', id)
    return render(request, 'manager/view.html', {'posts':posts})
