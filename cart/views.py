from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product
from .models import Wishlist



from .models import Cart
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def add_to_cart(request, product_id):
    # get product instance with given id
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = Cart.objects.get(user=request.user, product=product)
        cart_item.units += 1
        cart_item.save()
        messages.success(request, "Item added to Cart")
    except Cart.DoesNotExist:
        Cart.objects.create(user=request.user, product=product)
        messages.success(request, "Item added to Cart")

    return redirect('product:home')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, 'Item removed from Cart')

    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.units * item.product.unit_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, "cart/cart_detail.html", context)

@login_required
def increment_units(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.units += 1
        cart_item.save()

    return redirect('cart:cart_detail')

@login_required
def decrement_units(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        if cart_item.units > 1:
            cart_item.units -= 1
            cart_item.save()

    return redirect('cart:cart_detail')


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Prevent duplicate wishlist entries
    if Wishlist.objects.filter(user=request.user, product=product).exists():
        messages.info(request, "Item already in wishlist.")
    else:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, "Item added to wishlist.")

    return redirect('product:home')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    messages.success(request, "Item removed from wishlist.")
    return redirect('cart:view')


@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items
    }
    return render(request, "wishlist/wishlist.html", context)


@login_required
def stripe_checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('cart:cart_detail')

    total_price = sum(item.units * item.product.unit_price for item in cart_items)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'bdt',
                    'product_data': {
                        'name': 'Cart Purchase',
                    },
                    'unit_amount': int(total_price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/cart/payment-success/'),
            cancel_url=request.build_absolute_uri('/cart/payment-cancel/'),
        )
        return redirect(session.url)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def payment_success(request):
    Cart.objects.filter(user=request.user).delete()
    return render(request, "cart/payment_success.html")

def payment_cancel(request):
    return render(request, "cart/payment_cancel.html")