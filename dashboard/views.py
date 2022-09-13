
from django.shortcuts import redirect, render
from .models import Product, Order
from .forms import OrderForm, ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

    
# @login_required(login_url='user-login')

@login_required
def dashbord(request):
 
    return render(request, 'dashboard/dashbord.html')




# def product_delete(request, pk):
#     product = Product.objects.get(pk=pk)
#     product.delete()
#     return redirect('dashbord')
     

    # return render(request, 'dashboard/product_delete.html')
@login_required
def product(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form =  ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'products': products
    }

    return render(request, 'dashboard/product.html', context)

# @login_required
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    if request.method== 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
            
    else:
        form = ProductForm(instance=product)
    context ={
        'form': form
        

    }
    return render(request, 'dashboard/product_update.html', context)


# @login_required    



@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')
    
def index(request):
    orders = Order.objects.all()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('index')
    else:
        form = OrderForm()
    context={
        'orders': orders,
        'form': form,

    }
    return render(request, 'dashboard/index.html', context)


@login_required   
def order(request):
    orders = Order.objects.all()
    context ={
        'orders': orders
               
    }
    return render(request, 'dashboard/order.html', context)

