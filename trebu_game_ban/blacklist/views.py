from django.http import HttpResponse

# Create your views here.


def get():
    return HttpResponse("Esto es el get :D")


def post():
    return HttpResponse("Esto es el post :'D")
