from django.shortcuts import render, redirect
from .models import Product, CartItem, Review, Order, OrderItem
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm

def product_list(request):
    category = request.GET.get('category')
    sort_by = request.GET.get('sort')

    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    if sort_by == 'price':
        products = products.order_by('price')
    elif sort_by == 'name':
        products = products.order_by('name')

    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)
    return render(request, 'store/product_detail.html', {'product': product, 'reviews': reviews})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'items': items})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items.exists():
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart_items.delete()
        return render(request, 'store/order_success.html', {'order': order})
    return redirect('cart')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                return redirect('product_detail', pk=product.pk)
        else:
            form = ReviewForm()
    else:
        form = None

    return render(request, 'store/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })
