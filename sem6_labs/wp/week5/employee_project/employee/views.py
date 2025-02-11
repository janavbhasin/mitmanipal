from django.shortcuts import render
from datetime import datetime

# View to display the employee promotion form
def promotion_eligibility(request):
    if request.method == 'POST':
        # Get the employee id and the date of joining from the form
        employee_id = request.POST.get('employee_id')
        date_of_joining = request.POST.get('date_of_joining')
        
        # Convert the date of joining to datetime object
        try:
            doj = datetime.strptime(date_of_joining, '%Y-%m-%d')
            # Calculate years of experience
            years_of_experience = (datetime.now() - doj).days // 365
            
            # Check eligibility for promotion
            if years_of_experience > 5:
                eligible = "YES"
            else:
                eligible = "NO"
        except ValueError:
            eligible = "Invalid date format"

        return render(request, 'promotion_form.html', {'eligible': eligible})

    return render(request, 'promotion_form.html', {'eligible': None})
