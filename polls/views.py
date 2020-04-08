from django.shortcuts import render,redirect
from polls.form import taskInputForm
from polls.models import task
from django.views.decorators.http import require_POST

from rest_framework import viewsets
from .serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = task.objects.all()

def index(request):
    task_list = task.objects.order_by('id')
    form = taskInputForm()
    context = {
        'task_list':task_list,
        'form':form
    }
    return render(request,'index.html',context)

@require_POST
def addTask(request):
    form = taskInputForm(request.POST)
    if form.is_valid():
        newTask=task(status_task=request.POST['status_task'])
        newTask.save()
    return redirect('index')

def checkComplete(request,task_id):
    gettask = task.objects.get(pk=task_id)
    gettask.complete=True
    gettask.save()
    return redirect('index')

def checkUnComplete(request,task_id):
    gettask = task.objects.get(pk=task_id)
    gettask.complete=False
    gettask.save()
    return redirect('index')

def delete(request,task_id):
    gettaskDelete = task.objects.get(pk=task_id)
    gettaskDelete.delete()
    return redirect('index')
