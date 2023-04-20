from django.shortcuts import render
from djangoprj.models import Good


def index(request):
    goods = Good.objects.all()
    return render(request, 'index.html', context={'goods': goods, 'name': 'Kia Rio 3'})
