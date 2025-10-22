from django.shortcuts import render , redirect
from .models import Product , Category , Profile
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm , UpdateUserFrom , ChangePasswordForm , UserInfoForm
from payment.forms import shippingForm
from payment.models import ShippingAddress
import json
from cart.cart import Cart


def update_info(request):
    if not request.user.is_authenticated:
        messages.error(request, 'عدم دسترسی')
        return redirect('home')

    current_user = Profile.objects.get(user=request.user)
    shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)

    form = UserInfoForm(request.POST or None, instance=current_user)
    shipping_form = shippingForm(request.POST or None, instance=shipping_user)

    if form.is_valid() and shipping_form.is_valid():
        form.save()
        shipping_form.save()
        messages.success(request, 'تغییرات شما با موفقیت ذخیره شد.')
        return redirect('home')

    return render(request, 'update_info.html', {
        'form': form,
        'shipping_form': shipping_form
    })

def update_password(request):
     if request.user.is_authenticated:
          current_user = request.user
          if request.method == 'POST':
               form = ChangePasswordForm(current_user , request.POST)
               if form.is_valid():
                    form.save()
                    messages.success(request,'تغییرات شما با موفقیت ذخیره شد.')
                    login(request, current_user)
                    return redirect('update_user')
               else:
                    for error in list(form.errors.values()):
                         messages.error(request,'مشکلی پیش آمده است لطفا دوباره تلاش کنید.') 
                         return redirect('update_password')
          else:
               form = ChangePasswordForm(current_user)
               return render(request,'update_password.html' , {"form" : form})
     else :
          messages.error(request , 'عدم دسترسی')
          return redirect('home')
      
def update_user(request):
     if request.user.is_authenticated:
          current_user = User.objects.get(id=request.user.id)
          user_form = UpdateUserFrom(request.POST or None , instance=current_user)
          if user_form.is_valid():
               user_form.save()

               login(request, current_user)
               messages.success(request,'تغییرات شما با موفقیت ذخیره شد.')
               return redirect('home')
          return render(request,'update_user.html' , {'user_form': user_form })
     else :
          messages.error(request , 'عدم دسترسی')
          return redirect('home')

     return render(request , 'update_user.html' , {})

def category(request, foo=None):
    if request.method == 'POST':
        searched = request.POST.get('searched', '').strip()
        if searched:
            products = Product.objects.filter(name__icontains=searched)
            total = products.count()
            if total == 0:
                messages.error(request, 'محصول مورد نظر یافت نشد!')
                return redirect('category', foo='all')
            category_info = {"name": f"نتیجه جستجو برای: {searched}"}
            return render(request, 'category.html', {
                "products": products,
                "category": category_info,
                "total": total
            })
        else:
            return redirect('category', foo='all')

    foo = foo.replace('-', ' ')
    if foo == "all":
        products = Product.objects.all()
        total = products.count()
        category = {"name": "همه محصولات"}
    else:
        try:
            category = Category.objects.get(name=foo)
            products = Product.objects.filter(category=category)
            total = products.count()
        except Category.DoesNotExist:
            messages.error(request, "دسته‌بندی مورد نظر یافت نشد.")
            return redirect('home')

    return render(request, 'category.html', {
        "products": products,
        "category": category,
        "total": total
    })

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
               # Shoping cart 
               current_user = Profile.objects.get(user__id=request.user.id)
               saved_cart = current_user.old_cart

               if saved_cart:
                    converted_cart = json.loads(saved_cart)
                    cart = Cart(request)
                    for key , value in converted_cart.items():
                         cart.db_add(product=key, quantity=value)

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


