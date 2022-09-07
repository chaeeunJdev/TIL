from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash



# Create your views here.
def login(request):
    if request.user.is_authenticated: # 인증된 사용자라면
        # 로그인 뷰함수로 오면 안됨
        return redirect('articles:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data = request.POST) # 위 코드랑 같음

        # 검증
        if form.is_valid():
            # 검증통과하면 로그인  
            # save는 회원가입이고, 우리가 해야하는건 로그인(세션만들기)  
            auth_login(request, form.get_user())
            # next가 없으면 index로 가고 있으면 next파라미터를 처리하고 create로 가라.. 필수작업은 아님
            return redirect(request.GET.get('next') or 'articles:index')

    else :
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 회원가입 후 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else :
        form = CustomUserCreationForm()
    context = { # 검사통과 못했으면 에러메시지 담아서 출력
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    # 로그아웃 먼저 하고 탈퇴
    request.user.delete()
    # auth_logout(request)   # 필수는 아님
    return redirect('articles:index')


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user) # instance가 있어야 수정!
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else :
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else :
        form =  PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)