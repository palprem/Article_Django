from django.shortcuts import render
from .models import USER,ARTICLE

# Create your views here.
def register(request):
    if request.method=="POST":
        Fname= request.POST.get('Fname', '')
        Lname= request.POST.get('Lname', '')
        usarName= request.POST.get('usarName', '')
        PassWord = request.POST.get('PassWord', '')
        try:
            usarName2=USER.objects.get(usarName=usarName)
            return render(request, 'register.html',{"msg":"User Name Already Exist! Plz Login"})
        except:
            data=USER(Fname=Fname,
                    Lname=Lname,
                    usarName=usarName,
                      PassWord=PassWord)
            data.save()
            return render(request, 'login.html', {"msg":"Registration confirm"})
    return render(request, 'register.html')
    

def login(request):
    if request.method=="POST":
        usarName1= request.POST.get('usarName', '')
        PassWord1 = request.POST.get('PassWord', '')
        try:
            usarName=USER.objects.get(usarName=usarName1)
            PassWord=USER.objects.get(PassWord=PassWord1)
            try:
                cmpny=ARTICLE.objects.filter(user__usarName__contains=usarName1)
                return render(request, 'index.html',{'cmpny':cmpny,
                                                      'usarName':usarName1})
            except:
                return render(request, 'index.html',{'usarName':usarName1})
        except:
            return render(request, 'login.html', {"msg":"User Dose not exit! Plz Complite Registration"})
    return render(request, 'login.html')
        
def index(request):
    if request.method=="POST":
        atricle = request.POST.get('atricle')
        title = request.POST.get('title')
        img = request.POST.get('img')
        user_id = request.POST.get('user')
        print(user_id)
        user = USER.objects.get(usarName=user_id)
        print(user)
        data=ARTICLE(atricle=atricle,
                     title=title,
                     img=img,
                     user=user)
        data.save()
        try:
            cmpny=ARTICLE.objects.filter(user__usarName__contains=user_id)
            return render(request, 'index.html',{
              'usarName':user_id,
              'cmpny':cmpny
            })
        except:
            return render(request, 'index.html',{'usarName':user_id,})


    return render(request, 'index.html')








