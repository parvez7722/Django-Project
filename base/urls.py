from django.urls import path
from .views import myHeader,home,contact,product,signup,loginUser,new,detail,delete,logout_user

urlpatterns = [
    path('',myHeader,name='mainhome'),
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
    path('product/',product,name='product'),
    path('signup/',signup,name='signup'),
    path('login/',loginUser,name='login'),
    path('logout/',logout_user,name='logout'),
    path('new_item/',new,name='new'),
    path('product/<int:pk>/',detail,name='detail'),
    path('product/<int:pk>/delete/',delete,name='delete'),
]