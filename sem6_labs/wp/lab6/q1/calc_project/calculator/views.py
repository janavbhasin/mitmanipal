from django.shortcuts import render

def index(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Cannot divide by zero'

        except ValueError:
            result = 'Invalid input'

    return render(request, 'index.html', {'result': result})
