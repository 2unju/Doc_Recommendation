from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from models import Title, Content, DocUrl

# Create your views here.
def index(request):
    docs_list = Title.objcet.order_by('-_date')
    template = loader.get_template('DocList/index.html')
    return render(request, template, {
        'docs_list':
            docs_list,
    })

def docs(request, doc_id):
    title = get_object_or_404(Title, pk=doc_id)
    template = loader.get_template('DocList/docs.html')
    return render(request, template, {
        'title':
            title,
    })