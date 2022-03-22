from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Product
from django.contrib.auth import authenticate, login,  logout
from .forms import MyUserCreationForm 
  
products = [
        {'id':1, 'name':'WALI'},
        {'id':2, 'name':'PIZZA'},
        {'id':3, 'name':'BURGER'},
    ]

# Create your views here.
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/product.html', context)
    
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
      
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'user does not exist')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
    
def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form': form})
        

def home(request):
    # products = Product.objects.all()
    context = {'products': products}
    return render(request,'base/home.html', context)
