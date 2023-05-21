from wsgiref.simple_server import WSGIRequestHandler
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    paginator = Paginator(products, 9)  # Ограничение в 12 товаров на странице
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
       
    return render(request, 'shop/product/list.html', context={
        'category': category,
        'categories': categories,
        'products': products,
    })
    
    
@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', context={
        'product': product,
        'cart_product_form': cart_product_form,
    })


#-----------#
@login_required
def product_about(request):
    return render(request, 'shop/product/about.html')
