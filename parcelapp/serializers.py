from parcelapp.models import Branch, Agent, Parcel
from rest_framework import serializers

# Branch serializer
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

# Cargo/parcel Serializer
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

# Agent serializer
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'