from django.shortcuts import render, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'directory/index.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    pages = Page.objects.filter(category=category)
    return render(request, 'directory/category_detail.html', {'category': category, 'pages': pages})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'directory/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request, 'directory/add_page.html', {'form': form})
