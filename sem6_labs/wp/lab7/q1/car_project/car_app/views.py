from django.shortcuts import render

# View to display the form
def index(request):
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model_name = request.POST.get('model_name')
        return render(request, 'car_app/result.html', {'manufacturer': manufacturer, 'model_name': model_name})
    
    return render(request, 'car_app/index.html')

# View to display the result
def result(request):
    manufacturer = request.GET.get('manufacturer')
    model_name = request.GET.get('model_name')
    return render(request, 'car_app/result.html', {'manufacturer': manufacturer, 'model_name': model_name})
