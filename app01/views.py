from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from app01.forms import PostForm
# Create your views here.
def login1(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            username = postform.cleaned_data['username']
            password = postform.cleaned_data['password']
            #驗證該會員
            user = auth.authenticate(username=username,password=password)
            #通過驗證，並且帳號已經開始啟用
            if user is not None :
                message01 = '成功登入'
                #return redirect('/member1/')
                return render(request,'member1.html',locals())
            else:
                message01 = '帳號密碼有誤，無法登入'
        else:
            message01 = '圖形驗證錯誤'            
    else:        
        #這裡不是按post來的，表示式一開始顯示畫面時，要把所有表單驗證物件，傳到模板去
        postform = PostForm()
        message01 = '帳號，密碼，圖形驗證碼，都要輸入'
    return render(request,'login1.html',locals())

def member1(request):
    return render(request,'member1.html',locals())