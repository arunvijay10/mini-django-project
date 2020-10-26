from django.shortcuts import render, HttpResponse
from .models import Contact


# Create your views here.
def Formapp(request):
    if request.method == "POST":
        names = request.POST.get('names', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        sem = request.POST.get('sem', "")
        des = request.POST.get('des', "")
        passwd = request.POST.get('passwd', '')
        if names and email and phone and des and passwd:
            contact = Contact(names=names, email=email, phone=phone, des=des, passwd=passwd)
            contact.save();
        else:
            return HttpResponse("Invalid Performance ")

    return render(request, "form.html")
