from django.shortcuts import render

def index(request):
    context={'data':True}
    return render(request, "liftover/index.html", context)