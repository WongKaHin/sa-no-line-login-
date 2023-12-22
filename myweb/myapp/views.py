from email.policy import HTTP
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exchange, History, Member
import mysql.connector as sql

m=sql.connect(host="localhost",user="root",password="1234",database='sa2')

# Create your views here.
def index(request):
    return render(request,'index.html')

def member(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Member.objects.get(phone = current_user)
        exchs = Exchange.objects.all().filter(memid = account.memid)
        orders = History.objects.all().filter(memid = account.memid)
        print("\n\n\n\n\n",exchs)
        return render(request,'member.html',locals())
    else:
        return redirect(login)


def point(request):
    if 'user' in request.session:
        account = Member.objects.get(phone = request.session['user'])
        return render(request,'point.html',locals())
    else:
        return redirect(login)
    return render(request,"point.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    if request.method == "POST":
        if request.POST.get('submit')=='登入':
            phone = request.POST['username']
            password = request.POST['password']
            account = Member.objects.filter(phone = phone, password = password)
            if account:
                request.session['user'] = phone
                return redirect(member)
            else:
                return HttpResponse('Please enter valid Username or Password.')
        elif request.POST.get('submit')=='註冊':
            username = request.POST['username2']
            password = request.POST['password2']
            name = request.POST['fullname']
            con_password = request.POST['comfirm_password']
            if Member.objects.filter(phone=username).count()>0:
                return HttpResponse('用戶已存在')
            else:
                if password == con_password:
                    user = Member(phone = username, password = password, name = name, nickname = name, point = 0)
                    user.save()
                    return redirect('/')
                else:
                    return HttpResponse('密碼不一樣')
    else:
        return render(request,'login.html')



def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/')
    return redirect('/') 