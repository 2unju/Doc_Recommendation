from django.urls import path

from . import views

app_name = 'DocList'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doc_id>/', views.docs, name='docs'),
]