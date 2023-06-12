from django.shortcuts import render, redirect
from .models import Product, Supplier
from .forms import ProductForm, SupplierForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_product')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def update_qty(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('show_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_qty.html', {'form': form})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('show_product')
    return render(request, 'delete_product.html', {'product': product})

def show_product(request):
    products = Product.objects.all()
    return render(request, 'show_product.html', {'products': products})

def show_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'show_supplier.html', {'suppliers': suppliers})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_supplier')
    else:
        form = SupplierForm()
    return render(request, 'add_supplier.html', {'form': form})

def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(pk=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('show_supplier')
    return render(request, 'delete_supplier.html', {'supplier': supplier})
