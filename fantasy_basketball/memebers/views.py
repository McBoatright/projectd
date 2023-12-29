from django.http import HttpResponse
from django.template import loader
from .models import Memeber

def memebers(request):
  mymemebers = Memeber.objects.all().values()
  template = loader.get_template('all_memebers.html')
  context = {
    'mymemebers': mymemebers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymemeber = Memeber.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymemeber': mymemeber,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))