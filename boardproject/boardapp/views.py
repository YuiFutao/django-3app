from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
  if 'POST' == request.method:
    username2 = request.POST['username'] #htmlの中で「name="username"」として定義した値を取得
    password2 = request.POST['password']

    #既に同じ名前のユーザが存在した場合
    try:
      User.objects.get(username=username2)
      return render(request, 'signup.html', {'error':'このユーザは登録されています'} )

    # 重複が無かった場合(=正常にユーザ登録できる)
    except:
      user = User.objects.create_user(username2, '', password2)
      return render(request, 'signup.html', {'some':100})

  return render(request, 'signup.html', {'some':100})
