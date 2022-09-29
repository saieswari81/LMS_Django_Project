from rest_framework import serializers
from .models import Customer, LoanRules, LoanMaster


class CustomerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class LoanRulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanRules
        fields = '__all__'


class LoanMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanMaster
        fields = '__all__'


