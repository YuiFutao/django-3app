from django.http import HttpResponse
from django.views.generic import TemplateView
def helloworldfunction(request):
  returnobject = HttpResponse('Hello Django World')
  return returnobject
  

class helloworldView(TemplateView):
  template_name = 'hello.html'  #settings.py の DIRS に .html ファイルの場所を書く

