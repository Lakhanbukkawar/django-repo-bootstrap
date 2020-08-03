from django.shortcuts import render,HttpResponse
from app1.models import cust

# Create your views here.
def index(request):
    cob=cust.objects.all()

    contex={
        "cob":cob
    }
    return render(request,"dashboard.html",contex)