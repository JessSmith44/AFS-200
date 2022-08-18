from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path('', views.show_all_contacts),
    path('<int:contactid>', views.show_contact)
]