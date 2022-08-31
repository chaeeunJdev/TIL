from django.shortcuts import render
from .models import Article # 이걸 불러와야 Article.objects.all()이 가능
# Create your views here.
def index(request):
    # DB의 전체 데이터를 조회  
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # DB에 저장
    # 첫번째 방법
    #article = Article()
    #article.title = title # 위에서 get을 a로 받았으면 = a로 적어도 되지만 이름을 필드와 같게해주는게 좋음
    #article.content = content
    #article.save()

    # 두번째 방법
    # 왼쪽은 필드, 오른쪽은 사용자로부터 입력받은 데이터를 저장한 변수
    article = Article(title=title, content=content)
    article.save()

    # 세번째 방법
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')