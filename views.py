from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .models import Contact,MarksForm
# Create your views here.


#for displaying the contents of database in template or html page
def appFun(request):
    post=Blog.objects.all()
    return render(request,"static.html",{'post':post})

    
def appFun2(request):
    return HttpResponse("in first app second request or 2nd function")

#for displaying contents of html page to database... and again displaying it in webpage
def demo1(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        #message=request.POST['message']
        image=request.FILES.get('image')
        k=Contact(name=name,email=email,image=image)  #Contact is model name
        k.save()                                                      #contents gets saved in database
    return render(request,"static2.html")
def disp(request):
    post=Contact.objects.all()
    return render(request,"static2.html",{'post':post})

#for displaying contents of html page to database... and again displaying it in webpage
def marksForm(request):
    if request.method=='POST':
        name=request.POST['name']
        branch=request.POST['branch']
        year=request.POST['year']
        section=request.POST['section']
        marks=request.POST['marks']

        k=MarksForm(name=name,branch=branch,year=year,section=section,marks=marks)  #Contact is model name
        k.save()                                                      #contents gets saved in database
    return render(request,"static3.html")
def dispMarksForm(request):
    post=MarksForm.objects.all()
    return render(request,"static3.html",{'post':post})



"""def appFun3(request):
    post=AddBooks.objects.all()
    return render(request,"static.html",{'post':post})"""


""" def appFun3(request):
     post=Blog.objects.all()
     return render(request,"static.html",{'post':post})
    """ 