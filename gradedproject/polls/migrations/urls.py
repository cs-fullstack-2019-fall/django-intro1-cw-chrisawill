from django.urls import path

from . import views

urlpatterns = [
    path('MM/', views.index, name='index'),
    path('Buto/', views.index, name='Buto'),
    path('JB/', veiws.index, name='JB')
]