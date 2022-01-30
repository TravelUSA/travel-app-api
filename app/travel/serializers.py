from rest_framework import serializers
from core.models import Tag, Itenary


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ItenarySerializer(serializers.ModelSerializer):
    """Serializer for Itenary objects """     
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
