from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

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


def loginfunc(request):
  if 'POST' == request.method:
    username2 = request.POST['username'] 
    password2 = request.POST['password']

    user = authenticate(request, username=username2, password=password2)
    if user is not None:
      login(request, user)
      return redirect('list')

    else:
      return redirect('login')
  return render(request, 'login.html')


@login_required
def listfunc(request):
  object_list = BoardModel.objects.all()
  return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')

def detailfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
  post = BoardModel.objects.get(pk=pk)
  post.good += 1
  post.save()
  return redirect('list')

def readfunc(request, pk):
  post = BoardModel.objects.get(pk=pk)
  post.readtext
  loginuser = request.user.get_username()
  if loginuser in post.readtext:
    return redirect('list')
  else:
    post.read +=1
    post.readtext = post.readtext + ' ' + loginuser
    post.save()
    return redirect('list')

class BoardCreate(CreateView):
  template_name = 'create.html'
  model = BoardModel
  fields = ('title', 'content', 'author', 'images')
  success_url = reverse_lazy('list')
