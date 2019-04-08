from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>',views.delete, name="delete"),
    path('checked/<list_id>',views.checked, name="checked"),
    path('unchecked/<list_id>',views.unchecked, name="unchecked"),
]
