from django.shortcuts import render , redirect
from .models import Product , Category
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm , UpdateUserFrom


def update_user(request):
     if request.user.is_authenticated:
          current_user = User.objects.get(id=request.user.id)
          user_form = UpdateUserFrom(request.POST or None , instance=current_user)
          if user_form.is_valid():
               user_form.save()

               login(request, current_user)
               messages.success(request,'تغییرات شما با موفقیت ذخیره شد.')
               return redirect('home')
          return render(request,'update_user.html' , {'user_form': user_form})
     else :
          messages.error(request , 'عدم دسترسی')
          return redirect('home')

     return render(request , 'update_user.html' , {})


def category(request, foo):
    foo = foo.replace('-', ' ')
    if foo == "all":
        products = Product.objects.all()
        total = products.count()
        category = {"name": "همه محصولات"}
        return render(request, 'category.html', {
            "products": products,
            "category": category ,
            "total": total
        })
    else:
        try:
            category = Category.objects.get(name=foo)
            products = Product.objects.filter(category=category)
            total = products.count()
            return render(request, 'category.html', {
                "products": products,
                "category": category,
                "total": total
            })
        except Category.DoesNotExist:
            messages.error(request, "دسته‌بندی مورد نظر یافت نشد.")
            return redirect('home')

def product(request,pk):
     product = Product.objects.get(id=pk)
     return render(request , 'product.html' , {"product" : product })

def home(request) :
     products = Product.objects.all()
     return render(request , 'home.html' , {"products" : products })

# User Login Management
def login_user(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username , password=password) 
          if user is not None:
               login(request , user=user)
               messages.success(request, "شما با موفقیت وارد شدید")
               return redirect('home')
          else :
               messages.error(request, "مشکلی پیش آمد، دوباره تلاش کنید")
               return redirect('login')
     else:
          return render(request , 'login.html', {})

# User logout management
def logout_user(request):
     logout(request)
     messages.success(request, "شما با موفقیت خارج شدید")
     return redirect('home')

# Resgister user management 
def register_user(request):
     form = SignUpForm()
     if request.method == 'POST':
          form = SignUpForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data['username']
               password = form.cleaned_data['password1']
               user = authenticate(username=username,password=password)
               login(request, user)
               messages.success(request, "ثبت نام شما با موفیت انجام شد.")
               return redirect('home')
          else:
               messages.error(request, "مشکلی پیش آمد، دوباره تلاش کنید")
               return redirect('register')
     else :
          return render(request , 'register.html', {'form' : form})


