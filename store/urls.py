
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('book/<int:id>/',
         views.book_detail,
         name='book_detail'),

    path('register/',
         views.register,
         name='register'),

    path('login/',
         views.user_login,
         name='login'),

    path('logout/',
         views.user_logout,
         name='logout'),

    path('add-to-cart/<int:id>/',
         views.add_to_cart,
         name='add_to_cart'),

    path('cart/',
         views.cart_view,
         name='cart'),

    path('remove-from-cart/<int:id>/',
         views.remove_from_cart,
         name='remove_from_cart'),

    path('update-cart/<int:id>/',
         views.update_cart,
         name='update_cart'),

    path('place-order/',
         views.place_order,
         name='place_order'),

    
path('order-success/<int:order_id>/',
     views.order_success,
     name='order_success'),


path('my-orders/',
     views.my_orders,
     name='my_orders'),

]

