from django.shortcuts import render
from .models import Company


def Customer(request):
    co = Company.objects.filter(company_type_id=1)
    context = {'co': co}
    return render(request, 'customer/customer.html', context)


#def NewCustomer(request):

