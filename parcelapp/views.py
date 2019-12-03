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


class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
