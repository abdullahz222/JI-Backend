from rest_framework import serializers
from monthly_report.models import MemberData, Address, status
from phonenumber_field.serializerfields import PhoneNumberField


class MemberDataSerializer(serializers.ModelSerializer):
    mobile_number = PhoneNumberField()

    class Meta:
        model = MemberData
        fields = ['id', 'name', 'father_name', 'mobile_number',
                  'email', 'cnic', 'address', 'longitude','latitude',
                  'status_in_jamaat', 'designation', 'facebook_url', 'date_of_birth']


class AddressSerializer(serializers.Serializer):
    class Meta:
        model = Address
        fields = '__all__'
