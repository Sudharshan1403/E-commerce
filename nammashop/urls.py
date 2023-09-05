"""
URL configuration for IthuNammaKadai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('logout',views.logout_page,name='logout'),
    path('cart',views.cart_page,name='cart'),
    path('removecart/<str:cid>',views.remove_cart,name='removecart'),
    path('checkout/<str:cid>',views.checkout_page,name='checkout'),
    path('checkoutall',views.checkoutall_page,name='checkoutall'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('signup',views.signup,name='signup'),
    path('login',views.login_page,name='login'),
    path('collection',views.collections,name='collections'),
    path('collection/<str:name>',views.collectionsname,name='collections'),
    path('collection/<str:cname>/<str:pname>',views.product_details,name='product_details'),
   
]
