from django.urls import path
from . import views

app_name = "Loans"

urlpatterns = [
    path("", views.loan_list, name="loan_list"),
    path("create/", views.loan_create, name="loan_create"),
    path("<int:loan_id>/", views.loan_detail, name="loan_detail"),
    path("<int:loan_id>/update/", views.loan_update, name="loan_update"),
    path("<int:loan_id>/delete/", views.loan_delete, name="loan_delete"),
]
