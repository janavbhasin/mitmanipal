from django.shortcuts import render, redirect
from django.http import HttpResponse

# First page to collect user info
def first_page(request):
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Philosophy', 'Psychology', 'Business Management', 'Accounting']

    if request.method == 'POST':
        # Save form data to session
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')

        # Store the data in session
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject

        # Redirect to second page
        return redirect('second_page')

    return render(request, 'firstPage.html', {'subjects': subjects})

# Second page to display the info
def second_page(request):
    # Get the data from the session
    name = request.session.get('name', 'N/A')
    roll = request.session.get('roll', 'N/A')
    subject = request.session.get('subject', 'N/A')

    return render(request, 'secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })