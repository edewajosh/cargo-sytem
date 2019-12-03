import django_filters.rest_framework
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


class CustomerTrackCargo(generics.ListAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #permission_classes = [permissions.IsAuthenticated]
