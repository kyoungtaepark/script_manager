from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import ScriptlistModel, CommentModel
from .forms import ScriptlistForm, CommentForm

def index(request):

    if request.method == 'POST':
        forms = ScriptlistForm(request.POST, request.FILES)
        if forms.is_valid():
            newsrc = ScriptlistModel(
                            scrfile=request.FILES['scrfile'],
                            author=request.POST['author'],
                            tcid=request.POST['tcid'],
                            detail=request.POST['detail']
                            )
            newsrc.save()

            return HttpResponseRedirect(reverse('manager:index'))
    else:
        forms = ScriptlistForm

    scripts = ScriptlistModel.objects.all()

    return render(request, 'manager/index.html',{'scripts':scripts, 'forms' : forms})

def detail(request, id):
    '''
    id = ScriptlistModel.objects.filter(id =id )
    context = {'id': id}
    #scripts = ScriptlistModel.objects.filter(id = id)
    #script = {'author':scripts, 'scrfile' : scripts, 'tcid' : scripts, 'detail' : scripts, 'now' : scripts}
    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            newcom = CommentModel(
                            comments=request.POST['comments'],
                            writer=request.POST['writer'],
                            )
            newcom.save()

            return HttpResponseRedirect(reverse('manager:detail'))
    else:
        forms = CommentForm()
'''
    comments = CommentModel.objects.all()

    return render(request, 'manager/view.html' comments)

"""
    if request.method == 'POST':
        contents = ScriptlistForm(request.POST)
        files = ScriptlistForm(request.FILES)
        if contents.is_valid():
            contents.save()
            files.save()

            return HttpResponseRedirect(reverse('manager:index'))
    else:
        files = ScriptlistForm()

    scripts = ScriptlistModel.objects.all()

    return render(request, 'manager/index.html',{'scripts':scripts, 'forms' : forms})
"""