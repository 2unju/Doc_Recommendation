from django.urls import path

from . import views

app_name = 'DocList'
urlpatterns = [
    path('', views.main, name='main'),
    path('page/<int:_page>', views.index, name='index'),
    path('<int:_id>/', views.docs, name='docs'),
]