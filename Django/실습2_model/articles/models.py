from django.db import models

# 모델에서는 스키마의 뼈대를 만든다!

# Create your models here.
# Article 클래스는 models의 model클래스를 상속받아서 시작
class Article(models.Model):
    # <필드이름 = 타입> 순서로 지정
    title = models.CharField(max_length=10) # 필수키워드 존재
    content = models.TextField() # charfield보다 긴 텍스트를 제한
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    # shell에서 제목을 바로바로 보고싶다.
    def __str__(self):
        return self.title