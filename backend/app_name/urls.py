from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='BookView'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='BookDetailView'),
    path('factorial/', views.FactorialView.as_view(), name='FactorialView'),
    ]