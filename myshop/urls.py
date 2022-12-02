from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.product_list, name='product_list'),#отображение всего списка товаров на главной странице
    path('<slug:category_slug>/', views.product_list,#отображение по категориям
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug', views.product_detail,#тображение каждого по отдельности
         name='product_detail')
]