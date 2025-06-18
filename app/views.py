from django.shortcuts import render

# Create your views here.
def home(request):     #merr klikimin e linkut
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")