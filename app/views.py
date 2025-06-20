from django.shortcuts import render
from .models import *
from django.contrib import messages 

# Create your views here.
def home(request):    #merr klikimin e linku
    #te gjitha informacionet e nje modeli 
    #nga databaza ne view
    items = Item.objects.all()  #html perdor for in
    #nga view ne html
    context = {"items":items}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST" :
        #marrim ingormacionet nga inputet
        firstNameInput = request.POST['name']  #name eshte name qe ka inputi te contact
        lastNameInput = request.POST['lastname']
        emailInput = request.POST['email']
        commentInput = request.POST['comment']
        if firstNameInput != "" and lastNameInput != "" and emailInput != "" and commentInput != "":
            Contact(contact_name = firstNameInput,  #marrim modelin i bejme save
                contact_surname = lastNameInput,
                contact_email = emailInput,
                contact_comment = commentInput
                ).save()      
            messages.success(request, "message send")
        else:
            messages.error(request, "message not send")
                                
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

def details(request, id):
    itemInfos = Item.objects.get(pk=id) #behet dallimi nga id primary key
    context = {"itemInfos": itemInfos}  #key ne thonjeza e marrim nga key qe kemi ber te details ndersa value ia japim ne emer te ngjashem qe ta gjejme
    return render(request, "details.html", context)
