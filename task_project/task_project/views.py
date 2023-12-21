from django.shortcuts import render
from TaskModel.models import Task


def home(request):
    data = Task.objects.all()
    print(data)
    return render(request, 'index.html',{'data':data})