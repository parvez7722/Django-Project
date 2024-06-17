from django.shortcuts import render,redirect,get_object_or_404
from .models import Categorie,Product
from .forms import Formcreation,new_item
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def myHeader(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def detail (request,pk):
    item = get_object_or_404(Product,pk=pk)

    context = {
        'item' : item,
    }
    return render(request,'detail.html',context)

def delete(request,pk):
    item = get_object_or_404(Product,pk=pk,product_user=request.user)
    item.delete()

    return redirect('product')


def contact(request):
    return render(request,'contact.html')

def product(request):
    myProduct = Product.objects.filter()
    myCategorie = Categorie.objects.all()

    return render(request,'product.html',{
        'product' : myProduct,
        'categorie' : myCategorie,
    })

def signup(request):
    
    if request.method =='POST':
        form = Formcreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.error(request,"Please Enter the Passwords Correctly")
    else:
        form = Formcreation()

    context = {
        'form' : form,
    }
        
    return render(request,'signup.html',context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Enter your username or password correctly.")
            
    return render(request, 'login.html')

@login_required
def new(request):
    if request.method == "POST":
        form = new_item(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.product_user = request.user
            item.save()

            return redirect ('detail',pk = item.id)
 
    else:         
        form = new_item()
    
    return render(request, 'new_item.html',{
        'forms' : form ,
        'title' : 'New Item',
    })

@login_required
def logout_user(request):
    logout(request)

    messages.success(request,"you have logged out")

    return redirect('home')
        