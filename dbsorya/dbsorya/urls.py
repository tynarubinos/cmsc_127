from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('update-qty/<int:product_id>/', views.update_qty, name='update_qty'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('show-product/', views.show_product, name='show_product'),
    path('show-supplier/', views.show_supplier, name='show_supplier'),
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('delete-supplier/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
]
