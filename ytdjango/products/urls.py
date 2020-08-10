from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
  path('', views.index ),
  path('create/', views.product_create_view ),
  path('detail/<int:productId>', views.product_detail_view , name='detail'),
  path('delete/<int:productId>/', views.product_delete_view, name='product-delete' )
]