from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "Loans"

urlpatterns = [
    
    path("", views.loan_list, name="loan_list"),
    path("create/", views.loan_create, name="loan_create"),
    path("<int:loan_id>/", views.loan_detail, name="loan_detail"),
    path("login/", auth_views.LoginView.as_view(template_name="loans/login.html"), name="login"),
    path("<int:loan_id>/update/", views.loan_update, name="loan_update"),
    path("<int:loan_id>/delete/", views.loan_delete, name="loan_delete"),

    
    path("register/", views.register_user, name="register_user"),
]

