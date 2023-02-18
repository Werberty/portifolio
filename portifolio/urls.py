from django.urls import path

from portifolio import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('htmx/', views.teste_htmx, name='teste-htmx'),
    path('content/', views.content, name='content'),
    path('page-1/', views.page_1, name='page_1'),
    path('page-2/', views.page_2, name='page_2'),
    path('page-3/', views.page_3, name='page_3'),
]
