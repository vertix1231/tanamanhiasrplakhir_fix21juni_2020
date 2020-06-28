from django.conf.urls import url
from . import views
from artikel import views as artikelViews

urlpatterns = [
    url(r'^$',views.store,name='store'),
    url(r'^carts/$',views.cart,name='cart'),
    url(r'^cekot/$',views.checkout,name='checkout'),
    # url(r'^artikel/$',artikelViews.updateItem,name='update_item'),
    # url(r'^artikel/', include('artikel.urls', namespace='artikel')),
    # url(r'^process_order/$',views.processOrder,name='process_order'),
    # url(r'^update_item/$',storeViews.updateItem,name='update_item'),
    
]
