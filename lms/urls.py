from django.urls import path
from lms import views

urlpatterns = [
    path('customer/', views.ManageCustomer.as_view(), name='customer'),
    path('customer/<int:id>/', views.ManageCustomer.as_view(), name='customer'),
    path('loan_rules/', views.ShowLoanRules.as_view(), name='loan_rules'),
    path('loan_master/', views.ShowLoanMaster.as_view(), name='loan_master'),
    path('show_status_single_customer/', views.ShowLoanStatusSingleCustomer.as_view(), name='ls_sc'),
]
