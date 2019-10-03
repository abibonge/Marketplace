from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.utils import timezone
from django.views.generic.edit import CreateView
from django import forms



def productshome(request): #Change this to home page in product later
	products = Product.objects.order_by('-votes_total')
	return render(request, 'products/home.html',{'products':products}) # Change this to home page in product later

@login_required(login_url="/accounts/login")
def addListing(request): #Change this to home page in product later
	if request.method == 'POST':
		if request.POST['product_name'] and request.POST['product_description'] and request.POST['product_price'] and request.FILES['product_image'] and request.POST['product_stock']:
			category = Category.objects.all()
			product = Product()
			product.name 		= request.POST['product_name']
			product.description = request.POST['product_description']
			product.price 		=request.POST['product_price']	
			product.image 		= request.FILES['product_image']
			product.stock 		=request.POST['product_stock']	
			#product.available	=
			product.created 	=timezone.datetime.now()
			product.updated 	=timezone.datetime.now()
			product.votes_tot	= 1
			product.creator 	= request.user
			for x in category:
				if request.POST['product_category']==x.name:
					product.category=x
			product.save()
			return redirect('/products/'+str(product.id))
		else:
			return render(request, 'products/addListing.html', {'error':'Missing Required Fields'})
	else:
		return render(request, 'products/addListing.html') # Change this to home page in product later


def prod_detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'products/detail.html',{'product':product})

@login_required(login_url="/accounts/login")
def upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total +=1
		product.save()
		return redirect('/products/'+str(product.id))
	else:
		return redirect('/products/'+str(product.id))


	
# Create your views here.
