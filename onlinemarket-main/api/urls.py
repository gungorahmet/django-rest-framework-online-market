from django.urls import path
from api.views import ProductListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
]