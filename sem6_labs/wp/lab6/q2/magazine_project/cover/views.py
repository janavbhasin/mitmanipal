from django.shortcuts import render

def cover_form(request):
    if request.method == "POST":
        # Retrieve form values from the POST request
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        background_color = request.POST.get("background_color")
        font_size = request.POST.get("font_size")
        font_color = request.POST.get("font_color")
        image_url = request.POST.get("image_url")
        
        context = {
            "title": title,
            "subtitle": subtitle,
            "background_color": background_color,
            "font_size": font_size,
            "font_color": font_color,
            "image_url": image_url,
        }
        return render(request, "cover_form.html", context)
    
    return render(request, "cover_form.html")
