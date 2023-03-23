from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vitals_id/', views.detail, name='detail'),
    path('<int:vitals_id/enter-vitals', views.enter_vitals, name='enter_vitals')
]
