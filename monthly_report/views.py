from .models import Address, MemberData
from .serializers import AddressSerializer, MemberDataSerializer
from rest_framework import generics


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class MemberDataList(generics.ListCreateAPIView):
    queryset = MemberData.objects.all()
    serializer_class = MemberDataSerializer


class MemberDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MemberData.objects.all()
    serializer_class = MemberDataSerializer
