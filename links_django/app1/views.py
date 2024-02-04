import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app1.models import Links
from django.http import JsonResponse

@login_required
def index_page(request):
    return render(request, 'index.html')
@login_required
def history_page(request):
    all_links = Links.objects.all()
    return render(request, 'history.html', {'data': all_links})

def create(request):
    print (request.body)
    if request.method == "POST":
        data = json.loads(request.body)
        link = data['link']
        desc = data['description']
        links = Links()
        links.description = link
        links.link = desc
        links.save()
    return JsonResponse({'success': 'Успех'})
