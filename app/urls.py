from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('blog_details', views.blogDetails, name='blog_details'),
    path('shop_details', views.shopDetails, name='shop_details'),
    path('shop_grid', views.shopGrid, name='shop_grid'),
    path('shoping_cart', views.shopingCart, name='shoping_cart'),
    path('main', views.main, name='main'),
    path('manager', views.manager, name='manager'),
    path('create_products', views.createproduct, name='create_products'),
]