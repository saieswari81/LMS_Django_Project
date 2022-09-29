import decimal

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Customer, LoanMaster, LoanRules, CustomerLoansStatus
from .serializer import CustomerDetailSerializer, LoanRulesSerializer, LoanMasterSerializer
# Create your views here.


loan_rules = LoanRules.objects.all()


class ManageCustomer(APIView):

    def get(self, request, id=None, format=None):
        if id is not None:
            try:
                customer = Customer.objects.get(customer_id=id)
            except:
                return Response({'msg': 'id does not exists'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = CustomerDetailSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        customer = Customer.objects.all()
        serializer = CustomerDetailSerializer(customer, many=True)
        # print('type(serializer.data): ', type(serializer.data))
        # print('serializer.data: ', serializer.data)
        # for cust in customer:
        #     print('Name: ', cust.customer_name, type(cust.customer_name))
        #     print('Credit Score: ', cust.customer_creditscore, type(cust.customer_creditscore))
        #     print('Required Loan Amount: ', cust.customer_req_loanamount, type(cust.customer_req_loanamount))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CustomerDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Customer added succesfully'}, status=status.HTTP_201_CREATED)

    def patch(self, request, id=None, format=None):
        if id is not None:
            try:
                customer = Customer.objects.get(customer_id=id)
            except:
                return Response({'msg': 'id does not exits'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = CustomerDetailSerializer(customer, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            msg = 'Account Updated Successfully for ' + customer.customer_name
            return Response({'msg': msg}, status=status.HTTP_200_OK)
        return Response({'msg': 'id not provided'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        if id is not None:
            try:
                customer = Customer.objects.get(customer_id=id)
            except:
                return Response({'msg': 'id does not exits'}, status=status.HTTP_400_BAD_REQUEST)
            customer.delete()
            return Response({'msg': 'Account deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'msg': 'id not provided'}, status=status.HTTP_400_BAD_REQUEST)


# Note this is confidential data and must be shown only to the admin privilege users and not to all
class ShowLoanRules(APIView):
    def get(self, request, format=None):
        # loan_rules = LoanRules.objects.all()
        serializer = LoanRulesSerializer(loan_rules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Note this is confidential data and must be shown only to the admin privilege users and not to all
class ShowLoanMaster(APIView):
    def get(self, request, format=None):
        loan_master = LoanMaster.objects.all()
        serializer = LoanMasterSerializer(loan_master, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowLoanStatusSingleCustomer(APIView):

    def post(self, request, format=None):
        serializer = CustomerDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        # print(serializer.data.get('customer_id'))
        # print(serializer.data.get('customer_name'))
        # print(serializer.data.get('application_date'))
        # print(serializer.data.get('customer_creditscore'))
        # print(serializer.data.get('customer_req_loanamount'))
        # print(type(serializer.data))
        cs = serializer.data.get('customer_creditscore')
        crla = serializer.data.get('customer_req_loanamount')
        crla = decimal.Decimal(crla)
        result = []
        for lr in loan_rules:
            res = {}
            cs_limit = lr.creditscore_limit
            cs_offset = lr.creditscore_offset
            amt_limit = lr.amount_limit
            amt_offset = lr.amount_offset
            if cs_limit <= cs <= (cs_limit + cs_offset) and amt_limit <= crla <= (amt_limit + amt_offset):
                res['loan_type'] = lr.loan.loan_type
                res['interest'] = lr.interest
                res['duration'] = lr.duration_months
                result.append(res)
        # print('Result: ', result)

        # return Response(serializer.data, status=status.HTTP_200_OK)
        if result:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Sorry you did not qualify for loan'}, status=status.HTTP_200_OK)
