from django.urls import path
from home import views

urlpatterns = [
    path('products/', views.ProductView.as_view(), name='home'),
    path('demo/', views.DemoView.as_view(), name='demo'),
]
