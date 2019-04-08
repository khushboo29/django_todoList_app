from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method =="POST":
        form = ListForm(request.POST)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,("Item has been added to the list!"))
            return render(request,'home.html',context={'all_items':all_items})
            #return HttpResponse('Hello in post, welcome to the index page.')
        else:
            #all_items = List.objects.all()
            return render(request,'home.html',context={'form': form})

    else:
        all_items = List.objects.all()
        return render(request,'home.html',context={'all_items':all_items})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item has been deleted successfully!"))
    return redirect('home')

def checked(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')

def unchecked(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')