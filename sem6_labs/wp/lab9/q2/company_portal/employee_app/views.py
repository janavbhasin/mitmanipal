from django.shortcuts import render, redirect
from .forms import WORKSForm, CompanySearchForm
from .models import WORKS, LIVES

def insert_works(request):
    if request.method == 'POST':
        form = WORKSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_works')
    else:
        form = WORKSForm()
    return render(request, 'employee_app/insert_works.html', {'form': form})

def search_employees(request):
    results = []
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']
            results = WORKS.objects.filter(company_name=company).values('person_name')
            results = [
                {
                    'person_name': r['person_name'],
                    'city': LIVES.objects.filter(person_name=r['person_name']).first().city
                }
                for r in results if LIVES.objects.filter(person_name=r['person_name']).exists()
            ]
    else:
        form = CompanySearchForm()
    return render(request, 'employee_app/search_employees.html', {'form': form, 'results': results})
