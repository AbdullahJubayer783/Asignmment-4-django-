from django.shortcuts import render , redirect
from . import forms
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = forms.taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = forms.taskForm()
    return render(request, 'task.html',{'form' : form})

def edit_post(request , id):
    post = models.Task.objects.get(pk = id)
    print(post)
    form = forms.taskForm(instance=post)
    if request.method == 'POST':
        form = forms.taskForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task.html',{'form' : form})

def delete_post(request,id):
    post = models.Task.objects.get(pk = id)
    post.delete()
    return redirect("home")