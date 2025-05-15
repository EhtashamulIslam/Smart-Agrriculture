from django.urls import path

from . import views
from cart import views as cart_views
app_name = 'cart'

urlpatterns = [
    path("addtocart/<int:product_id>/", views.add_to_cart, name='addtocart'),
    path("removefromcart/<int:cart_item_id>/", views.remove_from_cart, name='removefromcart'),
    path("cart_detail", views.cart_detail, name='cart_detail'),

    path('increment_units/<int:cart_item_id>/', views.increment_units, name='increment_units'),
    path('decrement_units/<int:cart_item_id>/', views.decrement_units, name='decrement_units'),

    path('checkout/', views.stripe_checkout, name='stripe_checkout'),
    path('payment-success/', cart_views.payment_success, name='payment_success'),
    path('payment-cancel/', cart_views.payment_cancel, name='payment_cancel'),

    path('add/<int:product_id>/', views.add_to_wishlist, name='add'),
    path('remove/<int:product_id>/', views.remove_from_wishlist, name='remove'),
    path('', views.wishlist_view, name='view'),

]
