from django.shortcuts import render
from rest_framework import permissions

from parcelapp.models import Branch, Agent, Parcel
from parcelapp.serializers import BranchSerializer, AgentSerializer, ParcelSerializer
from rest_framework import generics


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAdminUser]

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAdminUser]

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class ParcelDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

# Customer can view the status of their cargo


class CustomerTrackCargo(generics.RetrieveAPIView):
    serializer_class = ParcelSerializer

    def get_queryset(self):
        """
        This view returns an cargo object that matches the parcel serial number
        for the currently authenticated customer
        """
        user = self.request.user
        sn = self.kwargs['serial_number']
        return Parcel.objects.filter(sender__username=user).filter(serial_number=sn)

    #permission_classes = [permissions.IsAuthenticated]
