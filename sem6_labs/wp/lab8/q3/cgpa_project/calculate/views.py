# calculate/views.py
from django.shortcuts import render, redirect

def page1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        total_marks = request.POST.get('total_marks')

        if name and total_marks:
            # Store data in session
            request.session['name'] = name
            request.session['total_marks'] = total_marks
            return redirect('page2')  # Redirect to page 2 to show result
    return render(request, 'calculate/page1.html')


def page2(request):
    name = request.session.get('name')
    total_marks = request.session.get('total_marks')

    if name and total_marks:
        try:
            total_marks = float(total_marks)  # Ensure marks are numeric
            cgpa = total_marks / 50  # CGPA calculation
        except ValueError:
            cgpa = None
    else:
        cgpa = None

    return render(request, 'calculate/page2.html', {'name': name, 'cgpa': cgpa})
