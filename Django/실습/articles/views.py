from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # request : 사용자의 요청 정보가 담겨있다.
    # 사용자에게 보여줄 화면 html 파일이름
    return render(request, "articles/index.html")

def greeting(request):
    # 화면에 필요한 데이터들
    foods = ["사과", "바나나", "코코넛"]
    info = {"name": "JEONGCHAEEUN"}
    text = {"word": "one two three four five six"}

    # 각 데이터들을 다시 context라는 큰 딕셔너리로 묶은 다음
    context = {
        "foods" : foods,
        "info" : info,
        "text" : text,
    }
    return render(request, "articles/greeting.html", context)

def dinner(request):
    foods = ["족발", "햄버거", "치킨", "초밥",]
    pick = random.choice(foods)
    mynumber = 11

    context = {
        "pick" : pick,
        "foods" : foods,
        "number" : mynumber,
    }
    return render(request, "articles/dinner.html", context)

def throw(request):
    return render(request,"articles/throw.html")

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get("message"))

    message = request.GET.get("message")

    context = {"message" : message}
    return render(request,"articles/catch.html", context)

def hello(request, name):
    context = {"name":name}
    return render(request, 'articles/hello.html', context)
