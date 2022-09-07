from socket import fromshare
from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     # input에 관련된 것들을 작성  

#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATION_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#         ]

#     title = forms.CharField(max_length=10) # Form에서 max_length는 필수는x
#     content = forms.CharField(widget=forms.Textarea)
#     # 드롭다운 만들기
#     # 선택인자를 위에 따로 만들어줘야함
#     nation = forms.ChoiceField(choices=NATION_CHOICES) # choices는 무엇을 선택할지에대한 옵션
    # 체크박스
    # pnation = forms.ChoiceField(choices=NATION_CHOICES, widget=forms.RadioSelect) # choices는 무엇을 선택할지에대한 옵션

class ArticleForm(forms.ModelForm):
    # 위젯
    title = forms.CharField(
        label='제목', # 라벨태그를 '제목'으로 바꿈
        widget=forms.TextInput(
            attrs={ # 어트리뷰트스라는 속성인자에 딕셔너리로 값을 준다
                'class' : 'my-title form-control', # 속성이름 : 값
                'placeholder' : 'Enter the title',
                'maxlength' : 10,   # 여기서쓰는 maxlength는 유효성검사에 영향을 주지 않음 
                # 그냥 입력이 10글자 까지만 가능하도록 막음
            }
        )
    )

    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs = {
                'class' : 'my-content form-control',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={    # 공백넣고 제출누르면 나옴! (데이터가 없는게 아니라 띄워쓰기처럼 공백을 줘야 나옴)
            'required': 'Please enter your content',
        }
    )

    # Meta 클래스
    class Meta :
        # 어떤 모델을 기반으로 할지
        model = Article # ()을 통해 호출하지 않음!! 인스턴스로 사용하지않고 참조값으로 활용하므로 ()쓰지않기
         # 어던 모델필드 중 어떤 것을 출력할지
        fields = '__all__' # all = Article에서 사용자로부터 입력을 받는 모든 필드
