from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('counts/', views.counts_board, name='counts'),
    path('risk/', views.risk, name='risk'),

]