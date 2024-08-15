from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm,AddRecordForm
from . models import Record


def home(request):

    records=Record.objects.all()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect('home')
        else:
            messages.success(request,"Invalid username or password")
            return redirect('home')
    else:
        return render(request,'app/home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')


def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registration Successfull")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'app/register.html',{'form':form})
    return render(request, 'app/register.html', {'form':form})



def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'app/customer_record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in to see details")
        return redirect('home')



def delete_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        messages.success(request, "Deleted Successfully")
    else:
        messages.error(request, "You must be logged in to delete")

    return redirect('home')

def add_new_record(request):
    form=AddRecordForm(request.POST)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                add=form.save()
                messages.success(request,"Added")
                return redirect('home')
        return render(request,'app/add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in..")
        return redirect('home')       

def update_record(request,pk):
    if request.user.is_authenticated:
        curr=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated")
            return redirect('home')
        return render(request,'app/update.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to update records")
