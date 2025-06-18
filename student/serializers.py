from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    roll_no = serializers.CharField(max_length=20)
