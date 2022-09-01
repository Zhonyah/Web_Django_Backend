from .models import tb_news
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

def handler404(request, exception):
    return render (request, 'Mywebsite/error404.html')

def index(request):
    content = tb_news.objects.all().order_by("-id")
    return render(request, 'Mywebsite/index.html',{'news':content})

def mydata(request):
    return render (request,'Mywebsite/mydata.html')

@permission_required('is_staff',login_url='/')
def addnews(request):
    return render (request, 'Mywebsite/addnews.html')

def result(request):
    name = request.POST['name_news']
    detail = request.POST['news_detail']
    mydata = {
        'name_news' : name,
        'name_detail' : detail
    }
    return render (request, 'Mywebsite/result.html',mydata)

def addnewsdata(request):
    #news_title	news_detail	news_photo	news_date	
    name = request.POST['name_news']
    news_detail = request.POST['news_detail']
    news_newfile = request.FILES['name_newfile']
    content = tb_news(news_title=name,news_detail=news_detail,news_photo=news_newfile)
    content.save()
    return redirect("/content")

@permission_required('is_staff',login_url='/')
def content(request):
    mydatanews = tb_news.objects.all()
    return render (request, 'Mywebsite/content.html',{'news':mydatanews})
def contentedit(request):
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)
    return render(request,'Mywebsite/contentedit.html',{'result':result})

def contentupdate(request):
    id = request.POST['id']
    name = request.POST['name_news']
    news_detail = request.POST['news_detail']

    try:
        news_newfile = request.FILES['name_newfile']
    except KeyError:
        news_newfile = None

    content = tb_news.objects.get(pk=id)
    content.news_title = name
    content.news_detail = news_detail
    if news_newfile is not None:
        content.news_newfile = news_newfile
    content.save()
    return redirect("/content")

def contentdelete(request):
    id = request.POST['id']
    content =tb_news.objects.get(pk=id)
    content.delete()
    return redirect("/content")

def contentshow(request):
    id = request.GET['id']
    content =tb_news.objects.filter(pk=id)
    return render (request, 'Mywebsite/contentshow.html',{'result':content})

def regisusers(request):
    return render (request, 'Mywebsite/regisusers.html')

def regis_usersdata(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username_ = request.POST['user']
    email_ = request.POST['email']
    passwordcode = request.POST['password']
    repassword = request.POST['re-password']

    if passwordcode == repassword:
        if User.objects.filter(username=username_).exists():
            messages.error(request,"User มีการใช้งานแล้ว")
            return redirect("/regisusers")
        elif User.objects.filter(email=email_).exists():    
            messages.error(request,"Email มีการใช้งานแล้ว")
            return redirect("/regisusers")
        else:
            user = User.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = username_,
            password = passwordcode,
            email = email_
            )
            user.save()
            return redirect("/login")
    else:
        messages.error(request,"Password ไม่ตรงกัน")
        return redirect("/regisusers")

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        return render (request, 'Mywebsite/login.html')

def logincheck(request):
    user = request.POST['user']
    code = request.POST['password']
    
    user = auth.authenticate(username = user,password = code)
    
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.error(request,"ไม่พบผู้ใช้งานในระบบ")
        return redirect('/login')

def logoff(request):
    auth.logout(request)
    return redirect('/login')

