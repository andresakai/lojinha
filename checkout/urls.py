from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(
        r'^adicionar/(?P<slug>[\w_-]+)/$',views.create_cartitem,name='create_cartitem'),
    path('', views.cart_item, name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
    re_path(r'^finalizando/(?P<pk>\d+)/paypal/$', views.paypal_view, name='paypal_view'),
    path('meus-pedidos/', views.order_list, name='order_list'),
    re_path(
        r'^meus-pedidos/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
]