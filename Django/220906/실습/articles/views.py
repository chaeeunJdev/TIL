from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe # GET인 요청에 대해서만 뷰함수 실행
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        # create
        form = ArticleForm(request.POST) # 데이터를 인자로 넣고 인스턴스를 받음
        # 유효성 검증
        if form.is_valid():
            article = form.save() # 유효성 검사를 통과했다면 저장하고 생성된 객체를 article에 저장
            return redirect('articles:detail', article.pk) # 생성된 객체를 저장해줬기때문에 article.pk로 pk를 불러올 수 있음
    else : # 원래는 POST가 아닌 모든 경우라는 뜻이었지만
            # 데코레이터를 쓰고 리스트를 통해 값을 두개만 줌으로써
            # 여기 else는 GET인 경우가 된다.
        # new
        # 인스턴스를 사용할 것이기 때문에 모듈을 호출해줘야함
        form = ArticleForm()    # 인스턴스 생성
    # 위에 POST인경우 is_valid에서 튕겨져 나올수도있으므로 
    # 아래 context는 else문 안에 있으면 안됨
    context = {
        'form' : form, # 위에 is_valid() 튕겨온 form은 에러메시지를 포함
        # 아래 else문에서 내려온 폼은 빈값 포함
    }
    return render(request, 'articles/create.html', context)


        


    # 사용자 데이터는 모두 request.POST에 있으므로 이걸통해받고
    # 나머지는 modelform 에서는 자동으로 매핑
    # form = ArticleForm(request.POST) # 데이터를 인자로 넣고 인스턴스를 받음

    # # 유효성 검증
    # if form.is_valid():
    #     article = form.save() # 유효성 검사를 통과했다면 저장하고 생성된 객체를 article에 저장
    #     return redirect('articles:detail', article.pk) # 생성된 객체를 저장해줬기때문에 article.pk로 pk를 불러올 수 있음
    
    # # 통과하지 못했다면
    # print(f"에러: {form.errors}")
    # #return redirect('articles:new')

    # # 에러메세지를 출력
    # context = {
    #     'form' : form, # 여기로 넘어온 form은 유효성검증에 실패한 form
    # }
    # # redirect가 아니라 에러의 원인을 보여주면서 그냥 new페이지로 돌아가기
    # return render(request, 'articles/new.html', context)




    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # # DB에 저장
    # # 1
    # # article = Article()
    # # article.title = title
    # # article.content = content
    # # article.save()

    # # 2
    # article = Article(title=title, content=content)
    # article.save()

    # # 3
    # # Article.objects.create(title=title, content=content)

    # # return render(request, 'articles/index.html')
    # # return redirect('/articles/')
    # # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    # if request.method == "POST": # 데코레이터를 써줬으므로 if문이 필요없어짐
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)

#     # instance인자가 있어야 장고는 수정사항으로 받아들임!
#     form = ArticleForm(instance=article) # edit.html에서 input태그에 value를 지정안해줘도 알아서 원래 데이터들을 표시해줌
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk) # if-else둘다 있는 공통문이므로 밖으로 빼줬음
    if request.method =="POST":
        form = ArticleForm(request.POST, instance=article) # 이 instance 값이 없으면 생성이고 있으면 수정된 값
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else :
         # instance인자가 있어야 장고는 수정사항으로 받아들임!
        form = ArticleForm(instance=article) # edit.html에서 input태그에 value를 지정안해줘도 알아서 원래 데이터들을 표시해줌
    
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

