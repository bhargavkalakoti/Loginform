from django.shortcuts import render
from testapp.form import Loginform

def form_view(request):
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            form.save()
    form=Loginform()   
    return render(request,'testapp/loginpage.html',{'form':form})


