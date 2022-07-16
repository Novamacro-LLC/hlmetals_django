from django.shortcuts import render, redirect
from .models import Company, Notes
from django.http import HttpResponse
from .form import Customer, Note


def customer(request):
    co = Company.objects.filter(company_type_id=1)
    context = {'co': co}
    return render(request, 'customer/customer.html', context)


def edit_customer(request, conum):
    if request.method == 'GET':
        co = Company.objects.filter(id=conum)
        note = Notes.objects.filter(company_id=conum)
        context = {'co': co, 'note': note}
        return render(request, 'customer/editcustomer.html', context)
    else:
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
        else:
            HttpResponse('Data is not valid and cannot be saved')
        redirect('customer')


def new_customer(request):
    if request.method == 'GET':
        return render(request, 'customer/newcustomer.html')
    else:
        form = Customer(request.POST)
        if form.is_valid():
            Company.company_type = 1
            form.save()
        else:
            HttpResponse('Data is not valid and cannot be saved.')
        redirect('customer')


def note(request, notenum):
    if request.method == 'GET':
        note = Notes.objects.filter(id=notenum)
        context = {'note': note}
        return render(request, 'note/noteedit.html', context)
    else:
        form = Note(request.POST)
        if form.is_valid():
            form.save()
        else:
            HttpResponse('Data is not valid and cannot be saved')
        redirect('customer')


