from django.urls import path,include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('profile/', views.vprofile, name="profile"),
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('menu_builder/',views.menuBuilder, name='menu_builder'),

    # category 
    path('menu_builder/category/<int:pk>/',views.fooditem_by_category, name='fooditem_by_category'),
    path('menu_builder/category/add/',views.add_category,name='add_category'),
    path('menu_builder/category/edit/<int:pk>/',views.edit_category,name='edit_category'),
    path('menu_builder/category/delete/<int:pk>/',views.delete_category,name='delete_category'),

    # add food item
    path('menu_builder/food/add/',views.add_food,name='add_food'),
    path('menu_builder/food/edit/<int:pk>/',views.edit_food,name='edit_food'),
    path('menu_builder/food/delete/<int:pk>/',views.delete_food,name='delete_food'),

  

]