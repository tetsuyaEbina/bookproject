#UserCreationFormは、Userの新規作成に特化したForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    # デフォルトで用意されているUserモデルでなく、別に作成したモデルを用いる
    class Meta:
        # 以下のように記述することで、formで受けとったデータをどのModelに保存するか、プラウザに表示する項目を指定できる
        model  = User #新しくユーザが登録された際に、Userモデルにデータを追加することをDjangoに伝える
        fields = ('username', )