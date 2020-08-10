from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Product
from .forms import ProductForm, RawProductForm
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
  products = Product.objects.all()
  my_context = {
    "my_text": "This is about us",
    "my_number": 123,
    "my_list": [1313, 4231, 312, "Abc"],
    "products": products
  }
  return render(request,'products/index.html', my_context)

# def product_create_view(request):
#   my_form = RawProductForm()
#   if request.method == "POST":
#     my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#       print(my_form.cleaned_data)
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)
#   context = {
#     "form": my_form
#   }
#   return render(request,'products/product_create.html', context)

# def product_create_view_raw(request):
#   context = {}
#   if request.method == "POST":
#     my_new_title = request.POST.get('title')
#     print(my_new_title)
#   # Product.objects.create(title=my_new_title)
#   return render(request,'products/product_create.html', context)

def product_create_view(request):
  initial_values = {'title': 'initial default'}
  obj = Product.objects.get(id=1)
  form = ProductForm(request.POST or None, initial=initial_values)
  # form = ProductForm(request.POST or None, instance=obj)

  if form.is_valid():
      print(form.is_valid)
      form.save()
      form = RawProductForm()

  context = {
    'form': form
  }
  return render(request,'products/product_create.html', context)

def product_detail_view(request, productId):
  # product = get_object_or_404(Product, id=productId)
  try:
    product = Product.objects.get(id= productId)
    print(product)
  except:
    raise Http404
  

  return render(request, 'products/product_detail.html', {'product': product})

def product_delete_view(request, productId):
  product = get_object_or_404(Product, id=productId)
  if request.method == "POST":
    product.delete()
    return redirect('../../')

  return render(request, 'products/product_delete.html', {'product': product})


