from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home.html')

# Metadata page view
def metadata(request):
    return render(request, 'metadata.html')

# Reviews page view
def reviews(request):
    return render(request, 'reviews.html')

# Publisher info page view
def publisher_info(request):
    return render(request, 'publisher_info.html')
