from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from products import views

# api router
router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'products')

urlpatterns = [
    path('api/v1/',  include(router.urls)),
    path('docs/', include_docs_urls(title='API DJANGO CRUD')),
]
# Compare this snippet from products/views.py:
# from django.shortcuts import render
# from rest_framework import viewsets
