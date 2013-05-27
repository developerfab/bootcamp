# Create your views here.
from django.http import HttpResponse

def home(request):
    print("Hola mundo")
    return HttpResponse("Hola mundo")

