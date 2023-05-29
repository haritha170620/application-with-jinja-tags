from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Haritha','age':20}
    return render(request,'wish.html',context=d)