from django.shortcuts import render

def student_form_view(request):
    return render(request, 'student_form/student_form.html')
