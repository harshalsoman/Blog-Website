from django.shortcuts import render,redirect
from .models import blogform
from .form import *
import glob
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def Home(request):
    all_previews = blogform.objects.all()
    #all_images = Image.objects.all()
    c= 0



    return render(request, 'Home.html', {'previews': all_previews} )


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request, ' Invalid Credentials')
            return redirect('/Login')
    else:
        return render(request, 'Login.html')
def Signup(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print("usersaved")
        return redirect('/index')
    else:
        return render(request, 'Signup.html')

def index(request):
    all_previews = blogform.objects.all()
    #all_images = Image.objects.all()
    return render(request, 'index.html', {'previews': all_previews})
def newblog(request):
     if request.method == 'POST':

        #form= DataForm(request.POST)
        Title = request.POST['Title']
        Date = request.POST['Date']
        Content = request.POST['Content']
        #form = DataForm(request.POST, request.FILES)
        #if form.is_valid():
        #form.save()
        Image = request.FILES['Image']
       # print(Title)
        ins = blogform(Title=Title,Date=Date, Content=Content, Image=Image)

        ins.save()


     form=DataForm()
     return render(request, 'newblog.html',{'form':form})

def post(request,pk):
    all_context = blogform.objects.get(id=pk)

    return render(request, 'post.html', {'Contexts': all_context})





