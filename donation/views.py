import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def donate(request):
    if request.method == 'POST':
        amount = int(float(request.POST['amount']) * 100)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Farmer Donation'},
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/donate/success/'),
            cancel_url=request.build_absolute_uri('/donate/cancel/'),
        )
        return redirect(session.url)
    return render(request, 'donation/donate.html')

def donation_success(request):
    return render(request, 'donation/success.html')

def donation_cancel(request):
    return render(request, 'donation/cancel.html')