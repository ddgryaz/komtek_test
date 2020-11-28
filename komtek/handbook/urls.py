from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('elements', views.elements, name='elements'),
    path('by_elements/<int:element_id>/', views.by_elements),
    path('by_elements', views.by_elements_basic, name='by_elements_basic'),
    path('handbooks_bydate', views.handbooks_bydate_basic, name='handbooks_bydate_basic')
]
