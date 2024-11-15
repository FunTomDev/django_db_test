from django.shortcuts import render
from .models import Products

# Create your views here.
def products(request):

	context = {

		"products": Products.objects.all()

	}

	return render(request, "products/products.html", context=context)

def product(request, id):

	product = Products.objects.get(id=id)

	context = {

		"name": product.name,
		"price": product.price

	}

	return render(request, "products/product.html", context=context)

def add_product(request):

	context = {
		"post_request": True,
	}

	if request.method == "POST":

		name = request.POST.get('product_name')
		price = request.POST.get('product_price')
		
		try:
			product = Products(name=name, price=price)
			product.save()
			context['error'] = False
		except:
		
			print("Some error happened while adding product to database. Not adding this item to database.")
			context['error'] = True		

	else:

		context = {

			"post_request": False,
			"error": False

		}

	return render(request, "products/add_product.html", context=context)
