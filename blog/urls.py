from django.urls import path,include
from . import views
urlpatterns = [
    
    path('create100/', views.create100),
    path('2/',views.post_list2,name='post_list2'),
    path('',views.post_list,name='post_list'),
    path('post/<int:pik>/', views.post_detail, name='post_detail'),

]
