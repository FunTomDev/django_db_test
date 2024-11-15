from django.urls import path

from . import views

urlpatterns = [

	path("", views.products, name="products"),
	path('<int:id>', views.product, name="product"),
	path('add_product', views.add_product, name="add product"),
	
]