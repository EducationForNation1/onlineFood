from django.shortcuts import render,get_object_or_404
from vendor.models import Vendor
from menu.models import Category, FoodItem
from django.db.models import Prefetch
from django.http import JsonResponse
from .models import Cart
# Create your views here.
def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active =True)
    vendor_count = vendors.count()
    context={
        'vendors':vendors,
        'vendor_count':vendor_count
    }
    return render(request, 'marketplace/listings.html',context)



def vendor_detail(request,vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug=vendor_slug)
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
       Prefetch(
           'fooditems',
           queryset=FoodItem.objects.filter(is_available=True)
       ) 
    )

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = None

    context={
        'vendor':vendor,
        'categories':categories,
        'cart_items':cart_items,
    }
    return render(request, 'marketplace/vendor_detail.html',context)

def add_to_cart(request,food_id=None):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            #Check if the food item exists
             try:
                foodItem = FoodItem.objects.get(id=food_id)
                #Check if the user has already added that food to the cart
                try:
                    chkCart = Cart.objects.get(user=request.user, foodItem=foodItem)
                    chkCart.quantity +=1
                    chkCart.save()
                    return JsonResponse({
                        'status':'success', 'message':'Increased the cart Quantity'
                    })
                except:
                    chkCart = Cart.objects.create(user=request.user, foodItem=foodItem, quantity=1)
                    return JsonResponse({
                        'status':'success', 'message':'Added the food to the cart'
                    })
             except:
                 return JsonResponse({
                        'status':'Failed', 'message':'Food Does not exists'
                    }) 
        else:
             return JsonResponse({
            'status':'failed', 'message':'Invalid request'
        })

    else:
        return JsonResponse({
            'status':'failed', 'message':'Please Login To Continue'
        })