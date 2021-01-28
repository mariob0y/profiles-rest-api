from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializes a namefield for testing APIView'''
    name = serializers.CharField(max_length=10)