from django.shortcuts import render,redirect

from . models import *
from datetime import date

# Create your views here.


def showalltask(request):
	alltask = Task.objects.all()
	return render(request,'showalltask.html',{'alltask':alltask})


def createtask(request):
	if request.method == "POST":
		Task.objects.create(
			taskname = request.POST['taskname'],
			taskcompletiondate = request.POST['taskcompletiondate'],
			taskdescription = request.POST['taskdescription']
		)
		alltask = Task.objects.all()
		return render(request,'showalltask.html',{'alltask':alltask})
	else:
		return render(request,'createtask.html')


def edit(request, id):
	task = Task.objects.get(id=id)
	print(task)
	return render(request,'edit.html',{'task':task})


def update(request, id):
	task = Task.objects.get(id=id)
	if request.method == "POST":
		task.taskname = request.POST['taskname']
		task.taskcompletiondate = request.POST['taskcompletiondate']
		task.taskdescription = request.POST['taskdescription']
		task.save()
		alltask = Task.objects.all()
		return render(request,'showalltask.html',{'alltask':alltask})
	
	
def delete(request, id):
	task = Task.objects.get(id=id)
	task.delete()
	alltask=Task.objects.all()
	return render(request,'showalltask.html',{'alltask':alltask})

