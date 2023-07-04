
from rest_framework import serializers
from api.models import Nicgangtok,Employee

#craete serializers here
class NicgangtokSerializer(serializers.HyperlinkedModelSerializer):
        nicgangtok_id=serializers.ReadOnlyField()
        class Meta:
          model=Nicgangtok
          fields="__all__"
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
        employee_id=serializers.ReadOnlyField()
        class Meta:
            model=Employee
            fields="__all__"