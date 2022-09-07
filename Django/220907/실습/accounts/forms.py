from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()    # UserCreationForm의 Meta를 상속받지만 model부분만 수정하겠다
        fields = UserCreationForm.Meta.fields + ('email',)  # 더 가져오고싶은 정보. 추가정보는 db필드에 있는 것중에 가져와야함

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 너무 많은 정보가 보여지므로 내가 원하는 정보만 출력하기
        fields = ('email', 'first_name', 'last_name',)