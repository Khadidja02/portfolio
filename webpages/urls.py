from django.urls import path
from .views import (
    index_view,
    portfolio_detail_view,
    
)

urlpatterns = [
     # Define the root URL pattern
    path('', index_view, name='index'),
    path('portfolio/<int:pk>/', portfolio_detail_view, name='portfolio_detail'),  # Portfolio detail
  
]