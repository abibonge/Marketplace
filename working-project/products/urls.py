from django.urls import path, include
from . import views

urlpatterns = [
    path('addListing', views.addListing, name='addListing_page'),
    path('<int:product_id>', views.prod_detail, name='prod_detail'),
    path('<int:product_id>/upvote', views.upvote, name='prod_upvote'),
    
    ]