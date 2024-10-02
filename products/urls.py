from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from products import views

# api router
router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'products')
router.register(r'sales', views.SalesView, 'sales')
router.register(r'clientes', views.ClientesView, 'clientes')
router.register(r'salescart', views.salesCartView, 'salescart')
router.register(r'users', views.UsersView, 'users')


urlpatterns = [
    path('api/v1/',  include(router.urls)),
    path('docs/', include_docs_urls(title='API DJANGO CRUD')),
]
# Compare this snippet from products/views.py:
# from django.shortcuts import render
# from rest_framework import viewsets
