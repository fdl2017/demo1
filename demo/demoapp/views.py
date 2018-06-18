from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
#from django.http import HttpResonpse

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render({}, request))


def test(request):
	return JsonResponse({"result":"OK","message":"Hello,lanlan"})
