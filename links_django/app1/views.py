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

def cert_page(request):
    return render(request, 'cert.html')

def create(request):
    print (request.body)
    if request.method == "POST":
        data = json.loads(request.body)
        link = data['link']
        desc = data['description']
        links = Links()
        links.description = desc
        links.link = link
        links.save()
    return JsonResponse({'success': 'Успех'})

def deleteRecord(request, id):
    print(id)
    if request.method == "POST":
        links = Links.objects.get(id=id)
        links.objects.delete()
    return JsonResponse({'success': 'Успех'})