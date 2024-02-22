from django.shortcuts import render ,HttpResponse,redirect
from django.views import View


def names(request):
       return redirect('/home/')
def contact(request):
       return HttpResponse("It is contact page")

def edit(request,rid):
       print("My Id is",rid)
       return HttpResponse("My Id number is"+rid)
def delete(request,rid):
       print("Delete the id",rid)
       return HttpResponse("Deleted the id"+rid)

class SimpleView(View):
       def get(self,request):
              return HttpResponse("Welcome to Simpleview")
def home(request):
       return render(request,'index.html')   

def hello(request):
       context ={}
       context['name']='dhinakaran.S'
       context['x']=200
       context['y']=100
       context['l']=[10,20,30,40,50]
       context['products']=[
                      {'id':1,'name':'samsung','cat':'mobile','price':56000},
                      {'id':2,'name':'Jeans','cat':'Clothes','price':5600},
                      {'id':3,'name':'adidas Shoes','cat':'Shoes','price':1600},
                      {'id':4,'name':'Shirts','cat':'Clothes','price':1000},
                      {'id':5,'name':'Vivo','cat':'mobile','price':66000}

                    ] 
       return render(request,'index.html',context)    